#!/usr/bin/env python
import pymysql 
from tools import get_db
import matplotlib.pyplot as plt

con = get_db()
cur = con.cursor()
date = []
googClose = []
aaplClose = []
with con:
    for i in range(2):
        cur.execute("SELECT * From history where company_id = %i"%(i))
        rows = cur.fetchall()
        for row in rows:
            if i == 0:
                date.append(row[0])
                googClose.append(row[3])
            if i == 1:
                aaplClose.append(row[3])
                




# Now put together a plot. 
    # Most of the work is done on a subplot or axis object
ax = plt.figure().add_subplot(111)
ax.scatter(date, googClose,c='g')
ax.scatter(date,aaplClose,c='r')
plt.title('goog vs aapl')
plt.xlabel('aapl close')
plt.ylabel('goog close')
plt.show()
