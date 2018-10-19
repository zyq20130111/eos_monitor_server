# -*- coding: utf-8 -*-
# filename: main.py
import web
import threading
import time
from handle import Handle
import sys

urls = (
    '/wx', 'Handle'
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
