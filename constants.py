#!/usr/bin/env python
import sqlite3

mdb_conn = sqlite3.connect('./data/movie_db')
mdb_cur = mdb_conn.cursor()