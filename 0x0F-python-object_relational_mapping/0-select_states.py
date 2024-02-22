#!/usr/bin/python3
import MySQLdb
import sys

""" lists all states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3]
    )
    cursor = db.cursor()

    query_3 = """
    SELECT * FROM states;
    """

    cursor.execute(query_3)
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()