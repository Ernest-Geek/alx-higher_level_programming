#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    # Execute the SQL query to select states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%'"

    # Execute the SQL query
    cur.execute(query)

    # Fetch all the rows resulting from the query and store them in rows
    rows = cur.fetchall()

    # Iterate through all the rows and print them
    for row in rows:
        print(row)

    # Close the cursor and the database connection to free up memory
    cur.close()
    db.close()
