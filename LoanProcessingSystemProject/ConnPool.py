# pip install mysql-connector-python-rf

import mysql.connector
from mysql.connector import errors
 
# create connection pool and fetch the first connection
db1 = mysql.connector.connect( user='root'
                              ,password='227pankaj27'
                              ,host='127.0.0.1'
                              ,database='loans'
                              ,pool_name='LoanDBConnPool'
                              ,pool_size=3)
                              
print("Connection db1:", db1.connection_id)

