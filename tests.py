import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, set_collector):
        collector = set_collector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre(self, set_collector):
        collector = set_collector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_book_genre(self, set_collector):
        collector = set_collector
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == 'Комедии'

    def test_get_books_with_specific_genre(self, set_collector):
        collector = set_collector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби']

    def test_get_books_genre(self, set_collector):
        collector = set_collector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Фантастика'}

    def test_get_books_for_children(self, set_collector):
        collector = set_collector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites(self, set_collector):
        collector = set_collector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, set_collector):
        collector = set_collector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, set_collector):
        collector = set_collector
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    @pytest.mark.parametrize('book_name', [
        "А",
        "Война и Мир",
        "Lorem ipsum dolor sit amet, consectetuer",
        "Lorem ipsum dolor sit amet, consectetue",
        "复写 复制 临摹 描摹 抄袭 仿效 模仿 印相 制拷贝",
        "!№;?*();?:%№%:,.?*",
        "          "
    ])
    def test_add_new_book_parametrized(self, set_collector, book_name):
        collector = set_collector
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()


