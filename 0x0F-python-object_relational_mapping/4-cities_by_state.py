#!/usr/bin/python3
''' Module that lists all states from the database '''
import sys
import MySQLdb

def cities_by_state(username, password, database):

    db = MySQLdb.connect(host='localhost',  port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT C.id, C.name, S.name from cities C, states S where state_id = id order by id;")
    state = cursor.fetchall()
    for s in state:
        print(s)
    db.close()

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    cities_by_state(username, password, database)
