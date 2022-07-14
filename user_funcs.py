import sys

def get_query_for_insert():
    try:
        id = int(input('Enter ID: '))
        name = str(input('Enter Name: '))
        mark1 = int(input('Enter 1st Mark: '))
        mark2 = int(input('Enter 2nd Mark: '))
        mark3 = int(input('Enter 3rd Mark: '))
        query = f"""
            INSERT INTO marks VALUES(
                {id},
                '{name}',
                {mark1},
                {mark2},
                {mark3}
            )
        """
        return id,query 
    except:   
        print('Invalid Inputs...!')
        sys.exit(1)

def get_query_for_delete():
    try:
        id = int(input('Enter Student ID: '))
        query = f"""
            DELETE FROM marks WHERE id = {id}
        """    
        return query
    except:
        print('Invalid Inputs...!')  
        sys.exit(1)