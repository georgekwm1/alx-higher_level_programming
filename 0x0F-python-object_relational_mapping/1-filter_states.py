#!/usr/bin/python3
import mysql.connector as myc
import sys

"""lists all states with a name starting with
 N (upper N) from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    db = myc.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3]
    )
    cursor = db.cursor()

    query_3 = f"""
    SELECT * FROM {sys.argv[3]}.states WHERE states.name LIKE 'N%';
    """
   
    cursor.execute(query_3)
    
    for row in cursor:
        print(row)
