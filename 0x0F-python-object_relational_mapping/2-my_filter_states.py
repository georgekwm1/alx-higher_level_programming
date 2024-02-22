#!/usr/bin/python3
import MySQLdb
import sys

"""takes in an argument and displays all values in the states table of
 hbtn_0e_0_usa where name matches the argument"""

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3]
    )
    cursor = db.cursor()

    query_3 = f"""
    SELECT * FROM {sys.argv[3]}.states WHERE states.name LIKE '{sys.argv[4]}';
    """

    cursor.execute(query_3)
    for row in cursor:
        print(row)
