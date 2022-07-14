import mysql.connector
from mysql.connector import Error
import db_funcs
import user_funcs

connection = db_funcs.create_db_connection('localhost','root','','python_mysql')

def insert_data(connection,id,query):
    try:
        q1 = f"SELECT * FROM marks WHERE id = {id}"
        result = db_funcs.read_query(connection,q1)
        if len(result) > 0:
            print('\nStudent Marks Already Added\n')
        else:
            message = "\nData Successfully Added...!\n"
            db_funcs.execute_query(connection,query,message)
    except Error as err:
        print(err) 

def get_all_data(connection):
    query = "SELECT * FROM marks"
    try:
        results = db_funcs.read_query(connection,query)
        if len(results) < 1:
            print('No Marks Added')
        else:
            for result in results:
                print(f"ID: {result[0]}")
                print(f"Name: {result[1]}")
                print(f"Mark 1: {result[2]}")
                print(f"Mark 2: {result[3]}")
                print(f"Mark 3: {result[4]}")
                print("\n")
    except Error as err:
        print(err)          

def delete_marks(connection,query):
    try:
        message = "\nData Successfully Deleted...!\n"
        db_funcs.execute_query(connection,query,message)
    except Error as err:
        print(err)

print('Hi! Please enter Find to find all data.\nEnter Insert to insert new data.\nEnter Delete to delete specific data.\nEnter Exit to exit from programme..!\n')
isExit = False
while isExit != True:
    option = str(input('>'))
    option = option.lower().replace(' ','')
    print("\n")
    if option == 'find':
        get_all_data(connection)
    elif option == 'insert':    
        id,query = user_funcs.get_query_for_insert()
        insert_data(connection,id,query)
    elif option == 'delete':
        query = user_funcs.get_query_for_delete()
        delete_marks(connection,query)
    elif option == 'exit':
        print('Exit from the Programme')
        isExit = True
    else:
        print('Invalid Option...!\n')   