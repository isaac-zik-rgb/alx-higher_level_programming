#!/usr/bin/python3
import MySQLdb
import sys
""" import all method of the class MySQLdb"""

def list_states(username, password, database):
     """
    Retrieve and display a list of states from the given MySQL database.

    Args:
        username (str): MySQL username for database access.
        password (str): MySQL password for database access.
        database (str): Name of the database to retrieve states from.

    Returns:
        None

    Function-level attributes:
        - None
    """
     
     db = MySQLdb.connect(host='localhost', port=3006, user=username, passwd=password, db=database)
     cursor = db.cursor()
     """Execute SQL query to retrieve states"""
     query = "SELECT * FROM states ORDER BY states.id ASC"
     cursor.execute(query)
     """fetch all rows"""
     rows = cursor.fetchall()

     for row in rows:
          print(row)

          """close connection"""
     cursor.close()
     db.close()
          
if __name__ == "__main__":

    if(len(sys.argv) != 4):
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)
        
