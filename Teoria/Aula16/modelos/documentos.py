from datetime import date


class Document:
    def __init__(self, authors = [], date = date.today()):
        self._authors = authors
        self._date = date
    def __str__(self):
        return f'Document: Authors: {self._authors}, Date: {self._date}'
    def get_authors(self):
        return self._authors
    def get_date(self):
        return self._date
    def add_author(self,author):
        self._authors.append(author)
    

class EMail(Document):
    def __init__(self, to ,subject = "", authors=[], date=date.today()):
        super().__init__(authors, date)
        self._to = to
        self._subject = subject
    def get_subject(self):
        return self._subject
    def get_to(self):
        return self._to
    def __str__(self):
        return f'EMail : to:{self._to}, subject:{self._subject} {super().__str__()}'

class Book(Document):
    def __init__(self,title, authors=[], date=date.today()):
        super().__init__(authors, date)
        self._title = title
    def get_title(self):
        return self._title
    def __str__(self):
        return f'Book: Title: {self._title} - {super().__str__()}'
    