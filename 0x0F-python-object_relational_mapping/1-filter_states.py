#!/usr/bin/python3
"""list all states with a name starting with \
N from the database hbtn_0e_0_usa"""
import MySQLdb
import sys



if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name
    LIKE BINARY '%N' ORDER BY states.id")
    rows = cur.fetchall()
    """print rows"""
    for row in rows:
        print(row)
        """close the connect in both database and cursor object"""
    cur.close()
    db.close()
