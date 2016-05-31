#!/usr/bin/env python

from controller.base import BaseController
from frameworks.bottle import view, static_file, template

class HomeController(BaseController):
    
    
    @view('home/index')
    def index(self):
        pass

    def movies_by_genre(self, genre):
        return template('home/category', genre=genre)