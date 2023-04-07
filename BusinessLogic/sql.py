import json
import mysql.connector
from BusinessLogic.assemble_payload import PayloadAssembler


class Handler(PayloadAssembler):
    def __init__(self, api_key: str, ticker: str, user='afpii', password='5.5x', host='localhost', database='afp_ii'):
        super().__init__(api_key, ticker)
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def cnx(self) -> (object, object):
        """
        Initializes setup conn and cursor for sql
        :return: tuple of connection and cursor objects
        """
        conn = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database
        )
        cursor = conn.cursor()
        return conn, cursor

    def insert(self, data: json, table: str) -> None:
        """
        Inserts merged_metrics values to phpmyadmin ticker_metrics table
        :param table: name of table to insert into
        :param data: ticker instance's data values to insert
        :return: None
        """
        conn, cursor = self.cnx()

        keys = ", ".join(data.keys())
        values = tuple(data.values())
        placeholders = ", ".join(["%s"] * len(data)) #placeholder for values
        sql = f"INSERT INTO {table} ({keys}) VALUES ({placeholders})"
        cursor.execute(sql, values)

        conn.commit()
        cursor.close()
        conn.close()

    def insert_sec_filings(self) -> None:
        """
        Inserts new SEC filings from FMP api into afp_ii.sec_filings.
        Duplicate rows not inserted due to unique constraint on table's link and finalLink columns.
        :return: None
        """
        for json_package in self.get_sec_filings():
            try:
                self.insert(json_package, "sec_filings")
                print("Row inserted successfully!")
            except mysql.connector.Error as e:
                if e.errno == 1062:
                    print("DUPLICATE ERROR: Row was not updated, it's already in the table.")
                else:
                    print(f"ERROR: {e}")

    #write same for balance sheet, cashflow, and income stmt

