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
        
        movies = (
                  ("Captain America: The Winter Soldier", "Marvel", "None", "WinterSoldier"),
                  ("Deadpool", "Marvel", "None", "Deadpool"),
                  ("Ouija", "Horror", "None", "Ouija"),
                  ("Sinister 2", "Horror", "None", "Sinister2"),
                  ("The Babadook", "Horror", "None", "TheBabadook"),
                  ("The Visit", "Horror", "None", "Visit"),
                  ("The Boy Next Door", "Horror", "None", "TheBoyNextDoor"),
                  ("The Woman in Black", "Horror", "None", "WomanInBlack")
            )
        cur.executemany("INSERT INTO Movies VALUES(?, ?, ?, ?)", (movies))
        conn.commit()



