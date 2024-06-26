#!/usr/bin/python3
''' Module that takes in an argument and displays all values.'''
import sys
import MySQLdb

def my_safe_filter_states(username, password, database, searchName):

    db = MySQLdb.connect(host="localhost",  port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * from states where name = %s order by id",(searchName,))
    state = cursor.fetchall()
    for s in state:
        print(s)
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searchName = sys.argv[4]

    my_safe_filter_states(username, password, database, searchName)
