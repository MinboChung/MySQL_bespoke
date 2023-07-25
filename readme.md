# Welcome to MySQL_bespoke repo
```
Hi,

My name is Minbo Chung.

Here, I would like to present an Object-oriented design to use the MySQL client module. 

My main motivation to implement this module is to have my own SQL client for python projects in future. 

I hope my initiative help the other develpers/engineers.

I dream to be one of engineers who contribute their passion and knowledge in helping and contributing the world.
```

## Software used for the development
```{Python}
Python --version 3.11.4
import mysql # python -m pip install mysql-connector-python
OS: Windows 
```

## MySQL_bespoke mapping
```
The class diagram to be presented.

main.py: To test MySQLConnector class.
mysql_bespoke.py: ...
my_credentials.py: ...
config.ini: Saving your oracle credentials. (Make one if you don't have)
Further implementation to be included ...

```
### config.ini
```
1. Make a file called config.ini in cred folder
2. Inside the file, write as below and save it.

[database]
username=your_username_oracle
password=your_password_oracle


---------------------------------------------------- 
To find your username and password they are in:
    Linux (including Ubuntu and CentOS):

    Global configuration file: /etc/mysql/my.cnf or /etc/my.cnf
    User-specific configuration file: ~/.my.cnf

    macOS:

    Global configuration file: /usr/local/etc/my.cnf or /etc/my.cnf
    User-specific configuration file: ~/.my.cnf

    Windows:

    Global configuration file: C:\ProgramData\MySQL\MySQL Server x.x\my.ini
    User-specific configuration file: C:\Users\<your_username>\.my.cnf

    Please note that the my.cnf file might not exist by default, especially in some newer installations. In such cases, you may need to create the file manually.

    If you cannot find the my.cnf file in the above locations, you can check the MySQL documentation or use the MySQL command-line tool to find the configuration file location:

    1.    Open a terminal (Linux/macOS) or Command Prompt (Windows).
    2.    Run the following MySQL command: SHOW VARIABLES LIKE 'my.cnf';

```

### Adding user to the localhost
```
Microsoft Windows [Version 10.0.19045.3208]                                                                             (c) Microsoft Corporation. All rights reserved.                                                                                                                                                                                                 C:\WINDOWS\system32>mysql --version                                                                                     mysql  Ver 8.0.25 for Win64 on x86_64 (MySQL Community Server - GPL)                                                                                                                                                                            C:\WINDOWS\system32>mysql                                                                                               ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)                                                                                                                                                              C:\WINDOWS\system32>mysql -u minbochung95@gmail.com                                                                     ERROR 1045 (28000): Access denied for user 'minbochung95@gmail.com'@'localhost' (using password: NO)                                                                                                                                            C:\WINDOWS\system32>mysql -u minbochung95@gmail.com -p                                                      Enter password: ************                                                                                            ERROR 1045 (28000): Access denied for user 'minbochung95@gmail.com'@'localhost' (using password: YES)                                                                                                                                           C:\WINDOWS\system32>mysql -u root                                                                                       ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)                                                                                                                                                              C:\WINDOWS\system32>mysql -u root -p                                                                                    Enter password:                                                                                                         ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)                                                                                                                                                              C:\WINDOWS\system32>mysql -u root -p                                                                                    Enter password: ************                                                                                            Welcome to the MySQL monitor.  Commands end with ; or \g.                                                               Your MySQL connection id is 24                                                                                          Server version: 8.0.25 MySQL Community Server - GPL                                                                                                                                                                                             Copyright (c) 2000, 2021, Oracle and/or its affiliates.                                                                                                                                                                                         Oracle is a registered trademark of Oracle Corporation and/or its                                                       affiliates. Other names may be trademarks of their respective                                                           owners.                                                                                                                                                                                                                                         Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.                                                                                                                                                                  mysql> CREATE USER 'minbochung95'@'localhost' IDENTIFIED BY 'password'                                                  -> ;                                                                                                                Query OK, 0 rows affected (0.03 sec)                                                                                                                                                                                                            mysql> select * from USER                                                                                                   -> ;                                                                                                                ERROR 1046 (3D000): No database selected                                                                                mysql> SHOW USER                                                                                                            -> ;                                                                                                                ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'USER' at line 1                                                                      mysql> clear                                                                                                            mysql> GRANT ALL PRIVILEGES ON *.* TO 'minbochung95'@'localhost';                                                       Query OK, 0 rows affected (0.01 sec)                                                                                                                                                                                                            mysql>  

```


## To preview markdown in VS code (Self note)
```
Markdown preview in VS code # command ctrl + shift + v
```

## ChatGPT says mysql-connector-python vs mysqlclient (For fun)
```
Both mysql-connector-python and mysqlclient are Python libraries that allow you to connect to and interact with a MySQL database from your Python code. However, there are some differences between the two:

Supported MySQL APIs:

mysql-connector-python: This library is the official MySQL connector provided by Oracle. It implements the MySQL Client/Server protocol and supports the X DevAPI for MySQL, which is a modern, asynchronous API for working with MySQL databases.
mysqlclient: This library is a fork of the older MySQLdb library and provides a traditional Python DB-API interface for MySQL. It implements the MySQL C API and is built on top of the MySQL client library.
Compatibility:

mysql-connector-python: It is compatible with both Python 2 and Python 3.
mysqlclient: It is specifically designed for Python 3 (Python 3.4 and later). If you are using Python 2, you should use MySQLdb instead.
Asynchronous Support:

mysql-connector-python: It offers support for asynchronous programming using the asyncio module, allowing you to create asynchronous applications that can work with MySQL.
mysqlclient: It does not natively support asynchronous programming. For asynchronous support in Python 3, you should use mysql-connector-python.
Installation:

mysql-connector-python: You can install it using pip with the following command: pip install mysql-connector-python
mysqlclient: You can install it using pip with the following command: pip install mysqlclient
Community and Maintenance:

mysql-connector-python: As the official MySQL connector, it is actively maintained and supported by Oracle.
mysqlclient: While it is a widely used library, its development may not be as actively maintained as the official connector.
Both libraries have their strengths and may be suitable for different use cases. If you are starting a new project with Python 3 and need asynchronous support, mysql-connector-python might be a better choice. However, if you are working with an existing project or need compatibility with Python 2, mysqlclient (or MySQLdb for Python 2) could be more appropriate.
```
