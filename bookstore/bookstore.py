class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def get_books(self):
        return self.books
        
    def add_book(self, book):
        self.books.append(book)
        
    def search_books(self, title=None, author=None):
        result = []
        if not author and not title:
            return result
        for book in self.books:
            if not author:
                if book.title.lower().find(title.lower()) != -1:
                    result.append(book)
            elif not title:
                if book.author == author:
                    result.append(book)
            else:
                if book.title.lower().find(title.lower()) != -1 and book.author == author:
                    result.append(book)
        return result
        
        
class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    def get_books(self):
        return self.books


class Book(object):
    def __init__(self, title, author=None):
        self.title = title
        self.author = author
        self.author.books.append(self)
        
    def __str__(self):
        return 'title: ' + self.title + ', author: ' + self.author.name
        
b1 = Bookstore("ollie")
borges = Author("Jorge Luis Borges", "Argentina")
ficciones = Book("Ficciones", author=borges)
b1.add_book(ficciones)

tom = Author('tom', 'US')
toms_book = Book('toms book', author=tom)
b1.add_book(toms_book)

laura = Author('laura', 'here')
lauras_book = Book('lauras book', author=laura)
b1.add_book(lauras_book)

print(b1.search_books("Ficciones"))
print(b1.search_books(author=laura))
print(b1.search_books("Ficciones", laura))
print(b1.search_books("Ficciones", borges))
print(b1.get_books())
