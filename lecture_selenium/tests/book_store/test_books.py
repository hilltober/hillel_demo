import pytest
import requests

from lecture_selenium.tests.book_store.page_book_store import \
    BookStorePageSelene, BookStorePageSelenium


@pytest.mark.usefixtures('demoqa')
class TestBookStoreSelene:
    AUTHORS = ['Kyle Simpson', 'Marijn Haverbeke']
    PUBLISHERS = ["O'Reilly Media", "No Starch Press"]
    store = BookStorePageSelene()

    @pytest.fixture(autouse=True)
    def open_store(self):
        self.store.open()
        self.store.clear_search_field()

    def test_author(self):
        author = self.AUTHORS[0]
        publishers = self.store.get_publishers_for_author(author)
        assert self.PUBLISHERS[0] in publishers  # Вірний видавець цього автора
        assert len(set(publishers)) == 1  # Нема інших видавців цього автора

    @pytest.mark.parametrize('publisher', PUBLISHERS)
    def test_publishers(self, publisher):
        self.store.do_search(publisher)
        publishers = self.store.get_publisher_names()
        assert len(publishers) >= 2  # Як мінімум, дві книги видавництва
        assert publisher in publishers  # Очікуваний видавець
        assert len(set(publishers)) == 1  # Тільки один видавець

    @pytest.mark.parametrize('author', AUTHORS)
    def test_is_image_ok(self, author):
        self.store.do_search(author)
        images = self.store.get_image_sources()
        results = [requests.get(image).status_code for image in images]
        assert results[0] == 200
        assert len(set(results)) == 1

    def test_sort_publishers(self):
        button = self.store.get_header_button('Publisher')
        publishers1 = self.store.get_publisher_names()
        button.click()
        publishers2 = self.store.get_publisher_names()
        assert publishers1 != publishers2
        button.click()
        publishers3 = self.store.get_publisher_names()
        assert publishers3 == publishers1


@pytest.mark.usefixtures('chrome')
class TestBookStoreSelenium:
    AUTHORS = ['Kyle Simpson', 'Marijn Haverbeke']
    PUBLISHERS = ["O'Reilly Media", "No Starch Press"]

    @classmethod
    def initialize_page(cls):
        driver = cls.driver
        cls.store = BookStorePageSelenium(driver=driver)

    @pytest.fixture(autouse=True)
    def init_driver(self):
        yield self.initialize_page()

    def test_1(self):
        self.store.open()
        assert self.store.get_name() == 'Book Store'
        headers = self.store.get_headers()
        sort_publishers_button = self.store.get_header_button('Publisher')
        sources = self.store.get_image_sources()
        pass
