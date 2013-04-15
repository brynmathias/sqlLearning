#!/usr/bin/env python
import sqlite3 as lite
import sys
import ystockquote
con = lite.connect('test.db')


def createTable(con):
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE prices(Company TEXT, Date INT,\
        Opening DECIMAL, Closing DECIMAL, High DECIMAL, Low DECIMAL,\
        Volume INT)")



def checkTable(con,table,args):
    """docstring for checkTable"""
    cur = con.cursor()
    sql = 'create table if not exists ' + table + ' %s'%args
    cur.execute(sql)
    pass


def addEntry(con,table,str):
    sql = "INSERT INTO %s%s"%(table,str)
    cur = con.cursor()
    cur.execute(sql)
    pass


table_args = '(Company TEXT, Date INT,\
        Opening DECIMAL, Closing DECIMAL, High DECIMAL, Low DECIMAL,\
        Volume INT)'

tabArgs = "({cname}, {year}, {opening}, {closing}, {high}, {low}, {volume})"

test = tabArgs.format(cname='GOOG',year=20120631,opening=10.3,closing=11.2,high=15.7,low=10.2,volume=20000)

def main():
    checkTable(con, "prices",table_args)
    
    """docstring for main"""
    pass
    
    


if __name__ == '__main__':
    main()