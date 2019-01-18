# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 05:04:16 2019

@author: Juber
"""

import tornado.ioloop
import tornado.web
from tornado_cors import CorsMixin
import pandas as pd
from tornado import gen
from tornado.httpclient import AsyncHTTPClient

class MainHandler(CorsMixin,tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
   
    def set_default_headers(self):
        self.set_header("Access-Constrol-Allow-Origin", "*")
        self.set_header("Access-Constrol-Allow-Headers", "Content-Type")
        self.set_header("Access-Constrol-Allow-Methods", "POST")
        
    def post(self):
        try:        
            data = tornado.escape.json_decode(self.request.body)
            return data
        except(Exception) as err:
            print(str(err))

    CORS_ORIGIN = "*"
    CORS_HEADERS = "*"
    CORS_METHODS = 'POST'

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def hello():
#    data = pd.read_json(request.data).reset_index()
    data = pd.Series(app.post()).to_frame()
    print(data)
    return 'Success'    
    
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Started")
    tornado.ioloop.IOLoop.current().start()
    print("En Route")


#python "D:\Anuj\Web App\TornadoCORS.py"