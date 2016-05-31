#!/usr/bin/env python
from api.baseApi import BaseApi
from api.error import Error
from frameworks.bottle import Bottle, response, static_file




class AppleTV(BaseApi):
    
    def __init__(self):
        pass
    
    def movie_genre(self, genre, movie):
        return static_file(movie, root='/movies/' + genre)
    
    def page_for_genre(self, genre):
        pass