#!/usr/bin/env python
from api.baseApi import BaseApi
from api.error import Error
from frameworks.bottle import Bottle, response, static_file, request
from api.appleTv import AppleTV
import sqlite3
import constants
import os, sys

class MovieApi(BaseApi):
    apple_tv_api = AppleTV()

    def __init__(self):
        pass

    def movie_genre(self, genre, movie):
        return static_file(movie + '.mp4', root='/movies/' + genre)

    def get_apple_tv(self, genre):
        return apple_tv_api.page_for_genre(genre)

    def post_movie(self, genre):
        title = request.json.get("title")
        description = request.json.get("desc")
        filename = request.json.get("filename")
        movie = (title, genre, description, filename)
        conn = constants.mdb_conn
        cur = constants.mdb_cur
        file = '/movies/' + genre + '/' + filename + '.mp4'
        print(file)
        if os.path.isfile(file):
            cur.execute("INSERT INTO Movies VALUES (?, ?, ?, ?)", movie)
            conn.commit()
            return dict(code=200, message="Movie posted! Thank you!", valid=True)
        else:
            return dict(code=404, message="File not found. Please re-upload the movie before posting again.", valid=True)


