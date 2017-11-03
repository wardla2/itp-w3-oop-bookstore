import pytest
from argparse import Namespace

from bookstore import Bookstore, Book, Author


@pytest.fixture
def fixtures():
    fix = Namespace()

    fix.borges = Author("Jorge Luis Borges", "AR")
    fix.poe = Author('Edgar Allan Poe', 'US')

    fix.ficciones = Book("Ficciones", author=fix.borges)
    fix.aleph = Book("The Aleph", author=fix.borges)
    fix.raven = Book("The Raven", author=fix.poe)

    return fix


def test_instantiate_bookstore():
    store = Bookstore("Rmotr's bookstore")
    assert store.name == "Rmotr's bookstore"
    assert store.get_books() == []


def test_add_book_to_bookstore(fixtures):
    store = Bookstore("Rmotr's bookstore")
    assert store.get_books() == []

    store.add_book(fixtures.ficciones)
    assert store.get_books() == [fixtures.ficciones]

    store.add_book(fixtures.raven)
    assert store.get_books() == [fixtures.ficciones, fixtures.raven]

    # Test second store
    second_store = Bookstore("Second bookstore")
    assert second_store.get_books() == []

    second_store.add_book(fixtures.raven)
    assert second_store.get_books() == [fixtures.raven]


def test_search_bookstore_by_book_title(fixtures):
    store = Bookstore("Rmotr's bookstore")

    store.add_book(fixtures.ficciones)
    store.add_book(fixtures.aleph)

    results = store.search_books(title='XYZ')
    assert results == []

    results = store.search_books(title='ficc')
    assert results == [fixtures.ficciones]

    results = store.search_books(title='The')
    assert results == [fixtures.aleph]

    store.add_book(fixtures.raven)
    results = store.search_books(title='The')
    assert results == [fixtures.aleph, fixtures.raven]


def test_search_bookstore_by_book_author(fixtures):
    store = Bookstore("Rmotr's bookstore")
    store.add_book(fixtures.ficciones)
    store.add_book(fixtures.aleph)

    austen = Author('Jane Austen', 'UK')

    results = store.search_books(author=austen)
    assert results == []

    results = store.search_books(author=fixtures.borges)
    assert results == [fixtures.ficciones, fixtures.aleph]

    results = store.search_books(author=fixtures.poe)
    assert results == []

    store.add_book(fixtures.raven)
    results = store.search_books(author=fixtures.poe)
    assert results == [fixtures.raven]
