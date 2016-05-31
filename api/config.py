#!/usr/bin/env python
import sqlite3
import constants
import os.path
from api.baseApi import BaseApi
from api.error import Error
from frameworks.bottle import Bottle, response, static_file


class ConfigApi(BaseApi):
    
    def __init__(self):
        pass
    
   
    def initialize_server(self):
        conn = constants.mdb_conn
        cur = constants.mdb_cur
        cur.execute("CREATE TABLE Movies(Title TEXT, Genre TEXT, Description TEXT, filename TEXT)")
        cur.execute("CREATE TABLE Genres(Name TEXT)")
        conn.commit()



