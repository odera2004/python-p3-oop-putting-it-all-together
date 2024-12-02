#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count ):
        self.title = title
        self._page_count = None
        self._page_count = page_count
        

    @property
    def page_count(self):
       return self._page_count
    
    @page_count.setter
    def page_count(self, value):
     if not isinstance (value, int):
        print("page_count must be an integer")
     else:
        self._page_count = value
    
    def turn_page(self):
       print("Flipping the page...wow, you read fast!")

    # @property
    # def turn_page(self):
    #    return self.turn_page
    
    # @turn_page.setter
    # def turn_page(self, turn_page):
    #    if not isinstance(turn_page, str):
    #       print("Flipping the page...wow, you read fast!")
    #       self._turn_page = turn_page
        
    pass
    
        