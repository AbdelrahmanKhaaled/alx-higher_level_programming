#!/usr/bin/python3
''' Module that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument. '''
import sys
import MySQLdb

def my_filter_states(username, password, database, searchName):

    db = MySQLdb.connect(host=localhost,  port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * from states where binary name = '{}' order by id".format(searchName))
    state = cursor.fetchall()
    for s in state:
        print(s)
    db.close()

if __name__ == __main__:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searchName = sys.argv[4]

    my_filter_states(username, password, database, searchName)
