import mysql.connector
import unittest

class MySQLDatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "123456"
        self.database = "moms"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print(f"Connected to the MySQL database: {self.database}")
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print(f"Disconnected from the MySQL database: {self.database}")
        else:
            print("No active database connection to close.")

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

    def fetch_data(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            return data
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
            return None
