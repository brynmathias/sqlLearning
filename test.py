#!/usr/bin/env python
import sqlite3 as sq
import sys
con = None

try:
    con =sq.connect('test.db')
    
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data
    
except sq.Error, e:
    print "Error %s:"%e.args[0]
    sys.exit(1) 