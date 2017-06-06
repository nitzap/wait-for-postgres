#/usr/bin/python2.4
#
#

import psycopg2

# Try to connect

try:
    conn=psycopg2.connect("dbname='postgres' user='postgres' host='db'")
except:
    print ("I am unable to connect to the database.")

cur = conn.cursor()
try:
    cur.execute("""SELECT 1""")
except:
    print ("I can't SELECT from bar")

rows = cur.fetchall()
print ("\nRows: \n")
for row in rows:
    print ("====")
    print (row)
    print ("====")
