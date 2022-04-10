#!/usr/bin/python3
''' Required'''


import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[
        1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities, states \
            WHERE states.name LIKE %s AND cities.state_id = states.id \
                ORDER BY cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    str = ""
    for row in query_rows:
        str = str + row[0] + ", "
    if (len(str) >= 2):
        str = str[:-2]
        print(str)
    else:
        print()
    cur.close()
    conn.close()
