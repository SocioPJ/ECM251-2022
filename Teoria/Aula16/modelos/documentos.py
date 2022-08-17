from datetime import date


class Document:
    def __init__(self, authors = [], date = date.today()):
        self._authors = authors
        self._date = date
    def __str__(self):
        return f'Document: Authors: {self._authors}, Date: {self._date}'
    def get_authors(self):
        return self._authors
    

class EMail(Document):
    pass

class Book(Document):
    pass