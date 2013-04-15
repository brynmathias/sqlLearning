#!/usr/bin/env python
import pymysql 

def get_db():
    return pymysql.connect(host="localhost",port=3306,user="bryn",
                           passwd="mypass",db="stocks")
    
    
    
def checkTable(con,table,args):
    """docstring for checkTable"""
    cur = con.cursor()
    # cur.execute("DROP TABLE "+table)
    sql = 'create table if not exists ' + table + ' %s'%args
    cur.execute(sql)
    pass
    
def addEntry(con,table,str):
    sql = "INSERT INTO %s VALUES%s"%(table,str)
    cur = con.cursor()
    cur.execute(sql)
    pass