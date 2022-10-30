from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Проверка добавления книг.
    def test_add_new_book_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1


    # Нельзя добавить одну и ту же книгу дважды.
    def test_add_new_book_сannot_add_same_book_twice(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_rating()) == 1

    # Нельзя выставить рейтинг меньше 1.
    def test_set_book_rating_сannot_rate_less_than_1(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    # Нельзя выставить рейтинг больше 10.
    def test_set_book_rating_сannot_rate_more_than_10(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 11)

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    # У не добавленной книги нет рейтинга.
    def test_get_book_rating_book_not_added_has_no_rating(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Гордость и предубеждение и зомби') == None

    # Добавление книги в избранное.
    def test_add_book_in_favorites_add_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
    def test_add_book_in_favorites_you_cannot_add_book_to_favorites_if_it_is_not_in_dictionary(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert collector.get_list_of_favorites_books() == []

    # Проверка удаления книги из избранного.
    def test_delete_book_from_favorites_remove_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert collector.get_list_of_favorites_books() == []

    # Вывод список книг с определенным рейтингом
    def test_get_books_with_specific_rating_displaying_list_books_with_certain_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)

        assert collector.get_books_with_specific_rating(5) == ['Гордость и предубеждение и зомби']