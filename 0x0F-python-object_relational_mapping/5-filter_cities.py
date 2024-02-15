#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    query = "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE BINARY %s\
            ORDER BY states.id"
    cur.execute(query, (argv[4],))

    rows = cur.fetchall()
    city_names = ', '.join(row[0] for row in rows)
    print(city_names)

    cur.close()
    db.close()
