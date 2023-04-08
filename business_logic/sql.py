import json
import mysql.connector
from business_logic.assemble_payload import ForSQL


class Handler(ForSQL):
    def __init__(self, api_key: str, ticker: str, user='afpii', password='5.5x', host='localhost', database='afp_ii'):
        super().__init__(api_key, ticker)
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    def cnx(self) -> (object, object):
        """
        Initializes setup conn and cursor for phpmyadmin connection
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
        Inserts values --> phpMyAdmin.afp_ii.table (param)
        :param data: ticker instance's json values to insert
        :param table: str name of table to insert into
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

    def update_ticker_metrics(self) -> None:
        """
        Ticker instance's merged_metrics (from FMP) --> afp_ii.ticker_metrics
        Duplicate rows are accepted
        :return: None
        """
        try:
            self.insert(self.merge_metrics(), "ticker_metrics")
        except mysql.connector.Error as e:
            print(f"ERROR: {e}")

    def update_sec_filings(self) -> None:
        """
        Ticker instance's SEC filings (from FMP) --> afp_ii.sec_filings table
        Duplicate rows not accepted (links and finalLinks unique)
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

    def update_balance_sheet(self) -> None:
        """
        Ticker instance's Balance sheet (from FMP) --> afp_ii.balance_sheet table
        Duplicate rows not accepted (links and finalLinks unique)
        :return: None
        """
        for json_package in self.get_balance_sheet_statement():
            try:
                self.insert(json_package, "balance_sheet")
                print("Row inserted successfully!")
            except mysql.connector.Error as e:
                if e.errno == 1062:
                    print("DUPLICATE ERROR: Row was not updated, it's already in the table.")
                else:
                    print(f"ERROR: {e}")

    def update_cash_flow_statement(self) -> None:
        """
        Ticker instance's Cash-flow Statement (from FMP) --> afp_ii.cash_flow_statement table
        Duplicate rows not accepted (links and finalLinks unique)
        :return: None
        """
        for json_package in self.get_cash_flow_statement():
            try:
                self.insert(json_package, "cash_flow_statement")
                print("Row inserted successfully!")
            except mysql.connector.Error as e:
                if e.errno == 1062:
                    print("DUPLICATE ERROR: Row was not updated, it's already in the table.")
                else:
                    print(f"ERROR: {e}")

    def update_income_statement(self) -> None:
        """
        Ticker instance's Income Statement (from FMP) --> afp_ii.income_statement table
        Duplicate rows not accepted (links and finalLinks unique)
        :return: None
        """
        for json_package in self.get_income_statement():
            try:
                self.insert(json_package, "income_statement")
                print("Row inserted successfully!")
            except mysql.connector.Error as e:
                if e.errno == 1062:
                    print("DUPLICATE ERROR: Row was not updated, it's already in the table.")
                else:
                    print(f"ERROR: {e}")

    def read(self, query: str) -> [tuple]:
        """
        :param query: str of full sql query to run
        :return: list of tuples for each row of table
        """
        conn, cursor = self.cnx()

        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
