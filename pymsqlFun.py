#!/usr/bin/env python

import pymysql 
from tools import get_db, addEntry, checkTable
import datetime
import time
import ystockquote
import pylab as pl


con = get_db()
cur = con.cursor()
# cur.execute('DROP TABLE *')
# cur.execute('DROP TABLE history')
tableName = 'prices'
tableFormat = '(Company TEXT, d DATE, Opening FLOAT, Closing FLOAT,\
                High FLOAT, Low FLOAT, Volume FLOAT)'
# additionString = '(Company TEXT, Year INT, Month INT, \
#                 Day INT, Opening DECIMAL, Closing DECIMAL, High DECIMAL, \
#                 Low DECIMAL, Volume INT)'





checkTable(con,"Company",'(id INT NOT NULL, name CHAR(30), ticker CHAR(10), PRIMARY KEY (id))')
checkTable(con,"history",'(date DATE NOT NULL, company_id INT NOT NULL,\
            opening DECIMAL(9,2), close DECIMAL(9,2), high DECIMAL(9,2),\
            low DECIMAL(9,2), volume INT, PRIMARY KEY (date,company_id),\
            FOREIGN KEY (company_id) REFERENCES Company(id))')
# date DATE NOT NULL, company_id NOT NULL, price DECIMAL(9,2), volume INT, PRIMARY KEY (date,company_id), FOREIGN KEY(company_id) REFERENCES company(id))')
tabArgs = "('{date}',{i}, {opening}, {closing}, {high}, {low}, {volume})"

companies = [("Apple INC", "AAPL"),("Google",'GOOG')]

def Fill():
    for i,company in enumerate(companies):
        addEntry(con,"Company","(%i,'%s','%s')"%(i,company[0],company[1]))
    with con:
        cur.execute("SELECT * From Company")
        rows = cur.fetchall()
        for row in rows:
            vals = ystockquote.get_historical_prices(row[2],
                                                    '20100610','20130610')
            for v in vals[1:]:
                addEntry(con,'history',tabArgs.format(i=row[0],date=v[0],
                opening=v[1],closing=v[4],high=v[2],low=v[3],volume=v[5]))



with con:
    cur.execute("SELECT * From Company")
    rows = cur.fetchall()
    for row in rows:
        print row
    cur.execute("SELECT * From history")
    rows = cur.fetchall()
    for row in rows:
        print row
cur.close()
con.close()