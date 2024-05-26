import mysql.connector
from mysql.connector import Error

class DBConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",  
            user="root",  
            passwd="12345678",  
            database="vitamilk_db",  
            port="3306"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetch_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()