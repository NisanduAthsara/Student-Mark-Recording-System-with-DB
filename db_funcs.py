import mysql.connector
from mysql.connector import Error
import sys

def create_db_connection(hostname,username,password,db):
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            passwd=password,
            database=db)    
        return connection
    except Error as err:
        print(err)   

def execute_query(connection,query,message):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(message)
    except Error as err:
        print(err)   

def read_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(err)
        sys.exit(1)