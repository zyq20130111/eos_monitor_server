# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import web
import MySQLdb
from config import Config

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

           list = [] 
           for field_desc in cursor.description:
               list.append(field_desc[0])

	   index = 0
           result = '{'

           for row in cursor.fetchall(): 
               result = result + '"' + list[index] + '":' + str(row[0])
               
               if (index < cursor.rowcount - 1):
                  result = result + ","

	       print(list[index])

               index = index + 1

           result = result + '}'
           return result

           cursor.close()
           db.close() 
       except Exception, Argument:
            return Argument
