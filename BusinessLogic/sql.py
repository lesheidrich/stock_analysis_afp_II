import json
import mysql.connector


class Handler:
    def __init__(self, user='afpii', password='5.5x', host='localhost', database='afp_ii'):
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

    def insert_ticker_metrics(self, merged_json: json) -> None:
        """
        Inserts merged_metrics values to phpmyadmin ticker_metrics table
        :param merged_json: ticker instance's merged_metrics json
        :return: None
        """
        conn, cursor = self.cnx()

        keys = ", ".join(merged_json.keys())
        values = tuple(merged_json.values())
        placeholders = ", ".join(["%s"] * len(merged_json)) #placeholder for values
        sql = f"INSERT INTO ticker_metrics ({keys}) VALUES ({placeholders})"
        cursor.execute(sql, values) #values replace placeholder here

        conn.commit()
        cursor.close()
        conn.close()

