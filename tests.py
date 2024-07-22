import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", ["a" * 41, "b" * 42])
    def test_add_new_book_name_too_long(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_existing_book(self, collector):
        collector.add_new_book("Книга1")
        collector.add_new_book("Книга1")
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self, collector):
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.get_book_genre("Книга1") == "Фантастика"

    @pytest.mark.parametrize("genre", ["Неизвестный жанр", ""])
    def test_set_book_genre_invalid_genre(self, collector, genre):
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", genre)
        assert collector.get_book_genre("Книга1") == ""

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Фантастика")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert "Книга1" in books
        assert "Книга2" in books

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        collector.add_new_book("Книга2")
        collector.set_book_genre("Книга2", "Ужасы")
        children_books = collector.get_books_for_children()
        assert "Книга1" in children_books
        assert "Книга2" not in children_books

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Книга1")
        collector.add_book_in_favorites("Книга1")
        favorites = collector.get_list_of_favorites_books()
        assert "Книга1" in favorites

    def test_add_nonexistent_book_in_favorites(self, collector):
        collector.add_book_in_favorites("Книга1")
        favorites = collector.get_list_of_favorites_books()
        assert "Книга1" not in favorites

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Книга1")
        collector.add_book_in_favorites("Книга1")
        collector.delete_book_from_favorites("Книга1")
        favorites = collector.get_list_of_favorites_books()
        assert "Книга1" not in favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Книга1")
        collector.add_book_in_favorites("Книга1")
        collector.add_new_book("Книга2")
        collector.add_book_in_favorites("Книга2")
        favorites = collector.get_list_of_favorites_books()
        assert "Книга1" in favorites
        assert "Книга2" in favorites
