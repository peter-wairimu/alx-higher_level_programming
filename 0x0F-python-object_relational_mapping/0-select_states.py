#!/usr/bin/python3

"""
A script that lists states from the databases
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], paswrd= sys.argv[2],db=sys.argv[3], port=3306)

    rel = db.cursor()
    rel.execute('SELECT * FROM states;')
    states = rel.fetchall()

    for state in states:
        print(state)