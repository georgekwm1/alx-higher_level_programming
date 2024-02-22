#!/usr/bin/python3
import MySQLdb
import sys

"""takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3],
          port="3306")
    
    cursor = db.cursor()
    query = f"""
SELECT cities.name
FROM cities  
INNER JOIN states ON states.id = cities.state_id 
WHERE states.name = '{sys.argv[4]}'
ORDER BY cities.id ASC;
"""
    cursor.execute(query)
    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))