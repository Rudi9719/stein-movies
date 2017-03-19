#!/usr/bin/env python
import sqlite3
import constants
import glob, os
from api.baseApi import BaseApi
from api.error import Error
from frameworks.bottle import Bottle, response, static_file


class ConfigApi(BaseApi):
    
    def __init__(self):
        pass
    
   
    def initialize_server(self):
        conn = constants.mdb_conn
        cur = constants.mdb_cur
        os.chdir("/movies")
        for file in glob.glob("*.mp4"):
            movie = (file[:-4], "Unclassified", "None", file)
            cur.execute("INSERT INTO Movies VALUES(?, ?, ?, ?)", (movie))
        conn.commit()



