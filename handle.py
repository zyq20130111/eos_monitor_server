# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import receive
import web
import reply

class Handle(object):
    def GET(self):
       try:
         data = web.input()
         if len(data) == 0:
            return "hello, this is handle view"

        except Exception, Argument:
            return Argument
