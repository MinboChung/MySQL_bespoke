##################################################################
#   File name: my_credentials.py                                 #
#   Written by: Minbo Chung                                      #
#   File created: 2023-07-23                                     #
##################################################################

from configparser import ConfigParser

class MyCredentials():
    def __init__(self):
        config = ConfigParser()
        # Create your own config.ini file in cred folder.
        config.read('./cred/config.ini')

        self.usrname = config.get('database', 'username')
        self.psw = config.get('database', 'password')
    
    def get_creds(self):
        return (self.usrname, self.psw)

if __name__=="__main__":
    x = MyCredentials()

    print(x.get_creds())