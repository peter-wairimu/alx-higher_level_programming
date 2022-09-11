#!/usr/bin/python3
"""
Lists values in states table where name matches the argument

"""

import sys
import MySQLdb

if __name__ == '__main':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    inject = db.cursor()
    inject.execute("SELECT * FROM states WHERE name =%s;", (sys.argv[4],))
    states = inject.fetchall()

    for state in states:
        print(state)
