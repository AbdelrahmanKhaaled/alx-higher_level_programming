#!/usr/bin/python3
''' Module that lists all states from the database '''
import sys
import MySQLdb

def list_AllStates(username, password, database):

    db = MySQLdb.connect(host="localhost", user=username,
                            passwd=password, db=database, port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * from states;")
    state = cursor.fetchall()
    for s in state:
        print(s)
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_AllStates(username, password, database)
