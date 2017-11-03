# OOP Bookstore

Today, we're in charge of migrating our Bookstore project into an Object Oriented approach. The functionality will remain similar, but we'll use OOP to model our system.

For this project we have identified 3 key classes: `Bookstore`, `Author` and `Book`.

A `Bookstore` will be the starting point. You'll be able to add books and search from books in a bookstore object. In the following example, we'll create a bookstore and assign a book to it:

```python
store = Bookstore("Rmotr's bookstore")
# No books yet
store.get_books() == []

# We create an author and book
borges = Author("Jorge Luis Borges", "Argentina")
ficciones = Book("Ficciones", author=borges)

# We add the book to the bookstore
store.add_book(ficciones)

store.get_books() == [<Object Book('ficciones')>]
```

The bookstore also has a "search" functionality. It works a little bit different than the previous one. In this case, you can search by book title or book author, or both title **and** author. The search method is the same one `search_books`, but you'll have to make it dynamic enough to support the three scenarios. Example:

```python
# Searching *just* by title:
store.search_books(title='raven')

# Searching *just* by author:
poe = Author('Edgar Allan Poe', 'US')
store.search_books(author=poe)

# Searching by both title *and* author:
poe = Author('Edgar Allan Poe', 'US')
store.search_books(title='raven', author=poe)
```

Finally, the `Book` and `Author` classes have special relationships between them, and we want you to pay special attention to it.

## Recommended path to test

You're welcome to choose your own way to work through this project. But given the structure of the classes, this is the path we suggest you to follow, the order to make the tests pass throughout the different test files.

**1. Author's attributes**

```bash
$ py.test test_authors.py -k test_author_creation
```

**2. Books's attributes**

```bash
$ py.test test_books.py
```

**3. Author's relationship with books**
_This is a special one because of the way we have to relate both authors with books and books with authors_

```bash
$ py.test test_authors.py -k test_get_books_from_author
```

**4. Bookstore Initialization**

```bash
$ py.test test_bookstore.py -k test_instantiate_bookstore
```

**5. Add Book to Bookstore**

```bash
$ py.test test_bookstore.py -k test_add_book_to_bookstore
```


**6. Search books by title**

```bash
$ py.test test_bookstore.py -k test_search_bookstore_by_book_title
```

**7. Search books by author**

```bash
$ py.test test_bookstore.py -k test_search_bookstore_by_book_author
```

