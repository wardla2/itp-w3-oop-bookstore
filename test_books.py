
from bookstore import Book, Author


def test_book_creation():
    borges = Author("Jorge Luis Borges", "AR")
    poe = Author('Edgar Allan Poe', 'US')

    ficciones = Book("Ficciones", author=borges)
    aleph = Book("The Aleph", author=borges)
    raven = Book("The Raven", author=poe)

    assert ficciones.title == "Ficciones"
    assert ficciones.author == borges

    assert aleph.title == "The Aleph"
    assert aleph.author == borges

    assert raven.title == "The Raven"
    assert raven.author == poe
le, "The Aleph")
        self.assertEqual(aleph.author, borges)

        self.assertEqual(raven.title, "The Raven")
        self.assertEqual(raven.author, poe)
