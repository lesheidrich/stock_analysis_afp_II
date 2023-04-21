import mysql.connector


class SQLLoginCRUD:
    user = 'afpii'
    password = '5.5x'
    host = 'localhost'
    database = 'afp_ii'
    table = 'users'

    @staticmethod
    def cnx() -> (object, object):
        """
        Initializes setup conn and cursor for phpMyAdmin connection
        :return: tuple of connection and cursor objects
        """
        conn = mysql.connector.connect(
            user=SQLLoginCRUD.user,
            password=SQLLoginCRUD.password,
            host=SQLLoginCRUD.host,
            database=SQLLoginCRUD.database
        )
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def read(query: str) -> [tuple]:
        """
        Reads all users from phpMyAdmin.afp_ii.users. Fully based on param query string.
        :param query: SELECT * FROM users WHERE username='admin'
        :return: List of tuples (each row is a tuple)
        """
        conn, cursor = SQLLoginCRUD.cnx()

        cursor.execute(query)

        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    @staticmethod
    def insert(query: str) -> None:
        """
        Inserts query --> phpMyAdmin.afp_ii.users
        :param query: 'bela', MD5('pwd'), 'apikey', '0', 'email', 'full name'
        :return: None
        """
        conn, cursor = SQLLoginCRUD.cnx()

        sql = f"INSERT INTO {SQLLoginCRUD.table}(username, pwd, api_key, is_admin, email, full_name) VALUES ({query})"
        cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_where(query: str) -> None:
        """
        Deletes where query --> phpMyAdmin.afp_ii.users
        :param query: username='bela'
        :return: None
        """
        conn, cursor = SQLLoginCRUD.cnx()

        sql = f"DELETE FROM {SQLLoginCRUD.table} WHERE {query}"
        cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update(condition: str) -> None:
        """
        Updates based on condition param --> phpMyAdmin.afp_ii.users
        :param condition: SET username='bill' WHERE username='bela'
        :return: None
        """
        conn, cursor = SQLLoginCRUD.cnx()

        sql = f"UPDATE {SQLLoginCRUD.table} {condition}"
        cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()
