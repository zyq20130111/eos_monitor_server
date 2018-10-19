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
               return "need sql param"

           inj_str = "exec|insert|delete|update|master|truncate|declare|drop"
           inj_stra = inj_str.split("|")

           for word in inj_stra:
               if((sql.find(word.lower()) != -1)  or (sql.find(word.upper()) != -1) ):
                   return "Illegal statement" 
     
            
           db = MySQLdb.connect(Config.DB_SERVER, Config.DB_USER, Config.DB_PWD, Config.DB_NAME, charset='utf8' )
           cursor = db.cursor()
           cursor.execute(sql)

           list = [] 
           for field_desc in cursor.description:
               list.append(field_desc[0])

	   index_row = 0
           result = '{['

           cursor.fetchall()
	   count = cursor.rowcount
           print count

           for row in cursor.fetchall(): 

               #处理一行
               col_s = "{"
               index_col = 0

               for col in list:
                  
                  col_s = col_s + '"' + list[index_col] + '":' + str(row[index_col])
 
                  if (index_col < len(list) - 1):
                      col_s = col_s + ","
                  else:
                      col_s = col_s + "}"

                  index_col = index_col + 1
               print index_row 	
               if(index_row < (count - 1)):
                  result = result + col_s + ","
 
               index_row = index_row + 1  

           result = result + ']}'

           cursor.close()
           db.close()

           return result
 
       except Exception, Argument:
            return Argument
