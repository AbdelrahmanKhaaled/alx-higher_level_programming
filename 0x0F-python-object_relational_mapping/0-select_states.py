#!/usr/bin/python3
''' lists all states from the database '''

import sys
import MySQLdb

if __name__ = "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                            passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * from states;")
    state = cursor.fetchall()
    for s in state:
        print(s)
    db.close()
