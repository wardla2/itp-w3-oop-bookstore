
from bookstore import Book, Author


def test_author_creation():
    borges = Author("Jorge Luis Borges", "AR")
    poe = Author('Edgar Allan Poe', 'US')

    assert borges.name == "Jorge Luis Borges"
    assert borges.nationality == "AR"

    assert poe.name == "Edgar Allan Poe"
    assert poe.nationality == "US"

def test_get_books_from_author():
    borges = Author("Jorge Luis Borges", "AR")
    ficciones = Book("Ficciones", author=borges)
    aleph = Book("The Aleph", author=borges)

    assert borges.get_books() == [ficciones, aleph]
