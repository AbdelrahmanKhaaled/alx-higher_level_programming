#!/usr/bin/python3
''' Module lists all states with a name starting
with N (upper N) from the database. '''
import sys
import MySQLdb


def filter_states(u, p, d):

    db = MySQLdb.connect(host='localhost', port=3306, user=u, passwd=p, db=d)

    cursor = db.cursor()
    cursor.execute("SELECT * from states order by id;")
    states = cursor.fetchall()
    for state in states:
        if (state[1][0] == "N")
            print(state)
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    filter_states(username, password, database)
