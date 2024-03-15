#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON states.id = state_id\
                WHERE BINARY states.name = %s\
                ORDER BY cities.id ", [argv[4]])
    rows = cur.fetchall()
    num_rows = cur.rowcount
    for row in rows:
        if num_rows > 1:
            print(row[0], end=", ")
        else:
            print(row[0])
        num_rows -= 1

    cur.close()
    db.close()
