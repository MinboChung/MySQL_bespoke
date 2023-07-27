##################################################################
#   File name: mysql_bespoke.py                                  #
#   Written by: Minbo Chung                                      #
#   File created: 2023-07-23                                     #
##################################################################

from abc import ABC, abstractmethod
from mysql import connector
from mysql.connector import Error
from my_credentials import MyCredentials

class MySQLConnector(ABC):

    sql_commands:dict = {
        '': "SELECT",
        '': "UPDATE",
        '': 'DELETE',
        '': 'INSERT INTO',
        '': 'CREATE DATABASE',
        '': 'ALTER DATABASE',
        '': 'CREATE TABLE',
        '': 'ALTER TABLE',
        '': 'DROP TABLE',
        '': 'CREATE INDEX',
        '': 'DROP INDEX',
    }

    def __init__(self, 
                 hst:str = None,
                 usr:str = None,
                 pw: str = None,
                 db: str = None):
        my_oracle_usr, my_oracle_pw = MyCredentials().get_creds()
        self.host = "localhost" if hst == None else hst
        self.usr = my_oracle_usr if usr == None else usr
        self.pw = my_oracle_pw if pw == None else pw
        self.db = db
        self.my_dbconnection = None

    def connect(self):
        try:
            self.mydb_connection = connector.connect(
                host=self.host,
                user=self.usr,
                password=self.pw
            )
            print("Successfully connected")
        except Error as e:
            print(f"The error {e} occured")

    def close_connection(self):
        if self.mydb_connection:
            self.mydb_connection.close()

        if not self.mydb_connection.is_connected():
            print(f"Successfully disconnected")

    ################################################################

    # Some of The Most Important SQL Commands
    #     SELECT - extracts data from a database
    #     UPDATE - updates data in a database
    #     DELETE - deletes data from a database
    #     INSERT INTO - inserts new data into a database
    #     CREATE DATABASE - creates a new database
    #     ALTER DATABASE - modifies a database
    #     CREATE TABLE - creates a new table
    #     ALTER TABLE - modifies a table
    #     DROP TABLE - deletes a table
    #     CREATE INDEX - creates an index (search key)
    #     DROP INDEX - deletes an index    
    
    def create_database(self, db_name: str=None):
        # 1. Check if the db_name is defined
        if not db_name:
            raise Exception("Database name needs to be defined.")

        # 2. Check mysql connection
        db_conn = self.mydb_connection
        if not db_conn.is_connected():
            db_conn.connect()
        my_cursor = db_conn.cursor()
        
        # 3. Check if the db_name already exist if not create
        existence_check_query = f"SHOW DATABASES"
        my_cursor.execute(existence_check_query)
        db_list = [x for x in my_cursor if x[0] == db_name]
        if len(db_list) > 0:
            print(f"CREATE TB: {db_name} already exist")
            return
        else:
            print(f"CREATE TB: {db_name} does not exist")

        # 4. Create db
        create_db_query = f"CREATE DATABASE {db_name}"
        my_cursor.execute(create_db_query)

        # 5. Check if the db is created
        existence_check_query = f"SHOW DATABASES"
        my_cursor.execute(existence_check_query)
        db_list = [x for x in my_cursor if x[0] == db_name]
        if len(db_list) > 0:
            print(f"CREATE TB: {db_name} created")
        else:
            print(f"CREATE TB: {db_name} failed to be created")


    def delete_database(self, db_name:str=None):
        # 1. Check if the db_name is defined
        if not db_name:
            raise Exception("Database name needs to be defined.")

        # 2. Check mysql connection
        db_conn = self.mydb_connection
        if not db_conn.is_connected():
            db_conn.connect()
        my_cursor = db_conn.cursor()
        
        # 3. Check if the db_name already exist if not create
        existence_check_query = f"SHOW DATABASES"
        my_cursor.execute(existence_check_query)

        db_list = [x for x in my_cursor if x[0] == db_name]
        if len(db_list) >= 1:
            print(f"DROP TB: {db_name} exists")
        else:
            print(f"DROP TB: {db_name} does not exist")
            return

        # 4. Delete db
        delete_db_query = f"DROP DATABASE {db_name}"
        my_cursor.execute(delete_db_query)

        # 5. Check if the db is deleted
        my_cursor.execute(existence_check_query)
        db_list = [x for x in my_cursor if x[0] == db_name]
        if len(db_list) == 0:
            print(f"DROP TB: {db_name} is removed")
        else:
            print(f"DROP TB: {db_name} is not removed")


if __name__ == "__main__":
    my_db_connection = MySQLConnector()
    my_db_connection.connect()
    my_db_connection.create_database(db_name="minbo_db")
    my_db_connection.delete_database(db_name="minbo_db")
    my_db_connection.close_connection()
    ...