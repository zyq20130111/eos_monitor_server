# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import web
import MySQLdb
import Config from config

class Handle(object):
    def GET(self):

       try:
           data = web.input()
           if len(data) == 0:
               return "hello, this is handle view"

           sql = data.sql
           if sql.strip()=='':
               return "sql is null"

           inj_str = "'|and|exec|insert|select|delete|update|count|*|%|chr|mid|master|truncate|char|declare|;|or|-|+|,|drop"
           inj_stra = inj_str.split("|")
     
            
           db = MySQLdb.connect(Config.DB_SERVER, Config.DB_USER, Config.DB_PWD, Config.DB_NAME, charset='utf8' )
           cursor = db.cursor()
           cursor.execute(sql)

           result = ""
           for row in cursor.fetchall():
               result = result + "," + str(row[0])
          
           return result

           cursor.close()
           db.close() 
        except Exception, Argument:
            return Argument
