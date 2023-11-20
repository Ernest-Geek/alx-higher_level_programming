#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Establishing a connection to the MySQL database"""
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()

    """Get the state name from the command line argument"""
    state_name = sys.argv[4]

    """Execute the SQL query to select states with the specified name"""
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}'"
             .format(state_name))
    cur.execute(query)

    """Fetch all the rows resulting from the query and store it in the rows"""
    rows = cur.fetchall()

    """Iterate through and print each row"""
    for row in rows:
        print(row)

    """Close the cursor and the database connection to free up memory"""
    cur.close()
    db.close()

