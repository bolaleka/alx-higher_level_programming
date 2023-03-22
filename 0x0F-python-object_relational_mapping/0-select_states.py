#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb

db = MySQLdb.connect(user='root', passwd='root', db='hbtn_0e_0_usa');
cur = db.cursor();

fullLine = ''
for line in open('0-select_states.sql'):
    tmpLine = line.strip()

    if tmpLine[0] == '#' or tmpLine[0] == '-':
        continue    
    fullLine += line
my_list = [x + ';' for x in fullLine.split(';') if x]
for item in range(len(my_list) - 1):
    cur.execute(my_list[item])
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for j in range(len(my_list)):
    print(rows[j]) 
cur.close()
db.close()
    
