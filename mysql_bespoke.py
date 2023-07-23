##################################################################
#   File name: mysql_bespoke.py                                  #
#   Written by: Minbo Chung                                      #
#   File created: 2023-07-23                                     #
##################################################################

from abc import ABC
from mysql import connector
from mysql.connector import Error
from my_credentials import MyCredentials

class MySQLConnector(ABC):
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
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error {e} occured")

    def close_connection(self):
        if self.mydb_connection:
            self.mydb_connection.close()

        if not self.mydb_connection.is_connected():
            print(f"Successfully disconnected")





if __name__ == "__main__":
    my_db_connection = MySQLConnector()
    my_db_connection.connect()
    my_db_connection.close_connection()