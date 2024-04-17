#!/usr/bin/python3
''' Module that lists all states from the database '''
import sys
import MySQLdb


def list_AllStates(username, password, database):

    db = MySQLdb.connect(host='localhost',  port=3306,
    user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * from states order by id;")
    state = cursor.fetchall()
    for s in state:
        print(s)
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_AllStates(username, password, database)
