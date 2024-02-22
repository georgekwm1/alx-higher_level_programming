#!/usr/bin/python3
import MySQLdb
import sys

"""lists all cities from the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3],
          port="3306")
    
    cursor = db.cursor()
    query = """
SELECT cities.id, cities.name, states.name
FROM states 
INNER JOIN cities ON states.id = cities.state_id 
ORDER BY cities.id ASC;
"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)