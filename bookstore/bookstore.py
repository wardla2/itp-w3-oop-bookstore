class Bookstore(object):
    def __init__(self, name):
        self.books = []
    
    def get_books(self):
        return self.books
        
    def add_book(self, book):
        self.books.append(book)
        
    def search_books(self, title=None, author=None):
        for book in self.books:
            if book.title == title:
                return book
        return None
        
        
        
        
    

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality


class Book(object):
    def __init__(self, title, author=None):
        self.title = title
        self.author = author
        
b1 = Bookstore("ollie")
borges = Author("Jorge Luis Borges", "Argentina")
ficciones = Book("Ficciones", author=borges)
b1.add_book(ficciones)
b1.get_books()
print(b1.search_books("ficciones"))
#print(b1.get_books())
