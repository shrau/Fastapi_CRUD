import mysql.connector
from config.database_config import *


class DatabaseOperations:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=password,
        database=database_name
    )
    

    def execute_query(self,query):
        mycursor = self.mydb.cursor()
        mycursor.execute(query)
        return mycursor

    def commit_connection(self):
        self.mydb.commit()




