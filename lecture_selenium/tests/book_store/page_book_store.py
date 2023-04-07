from selenium.webdriver.remote.webdriver import WebDriver
from selene.api import s, ss, by, have, query, browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from lecture_selenium.tests.book_store.book_store_page_abs import BookStorePage


class BookStorePageSelene(BookStorePage):
    URL = 'books'

    def __init__(self):
        self.__store_name = s(by.class_name('main-header'))
        self.__search_field = s(by.id('searchBox'))
        self.__book_list_body = s(by.class_name('rt-tbody'))
        self.__header_bar = s(by.class_name('rt-tr'))
        self.__headers = self.__header_bar.ss(
            by.xpath('//div[contains(@class, "content")]'))
        self.__books = s(by.xpath(
            '//div[@role="row"][not(contains(@class, "pad"))]'
            '[contains(@class, "odd") or contains(@class, "even")]'))

    def open(self):
        browser.open(self.URL)
        return self

    def _get_element_locator_by_header_name(self, header):
        column_index = self.get_headers().index(header)
        raw_locator = self.__books._locator._description
        locator = f"//{''.join(raw_locator.split('//')[1::])[:-3:]}" \
                  f"/div[{column_index + 1}]"
        return locator

    def get_name(self) -> str:
        return self.__store_name.get(query.text)

    def get_headers(self) -> list:
        self.__headers.should(have.size_greater_than_or_equal(1))
        return [
            header.get(query.text)
            for header in self.__headers
            if len(header.get(query.text)) > 0]

    def get_header_button(self, name):
        self.__headers.should(have.size_greater_than_or_equal(1))
        return [header for header in self.__headers
                if header.get(query.text) == name][0]

    def get_header_elements(self, header_name):
        return ss(self._get_element_locator_by_header_name(header_name))

    def get_publisher_names(self) -> list:
        elements = self.get_header_elements('Publisher')
        return [data.get(query.text) for data in elements]

    def get_authors(self) -> list:
        elements = self.get_header_elements('Author')
        return [data.get(query.text) for data in elements]

    def get_image_sources(self) -> list:
        locator = f'{self._get_element_locator_by_header_name("Image")}//img'
        elements = ss(locator)
        return [data.get(query.attribute('src')) for data in elements]

    def get_publishers_for_author(self, author) -> list | str:
        self.do_search(author)
        assert len(set(self.get_authors())) <= 1, 'More than one author here!'
        return self.get_publisher_names()

    def clear_search_field(self):
        self.__search_field.clear().press_enter()

    def do_search(self, search_string):
        self.__search_field.set(search_string).press_enter()


class BookStorePageSelenium(BookStorePage):
    URL = 'https://demoqa.com/books'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.__store_name_loc = (By.CLASS_NAME, 'main-header')
        self.__search_field_loc = (By.ID, 'searchBox')
        self.__book_list_body_loc = (By.CLASS_NAME, 'rt-tbody')
        self.__header_bar_loc = (By.CLASS_NAME, 'rt-tr')
        self.__headers_loc = (
            By.XPATH, '//div[@class="rt-tr"]'
                      '//div[contains(@class, "content")]')
        self.__books_loc = (
            By.XPATH,
            '//div[@role="row"][not(contains(@class, "pad"))]'
            '[contains(@class, "odd") or contains(@class, "even")]')

    def open(self):
        self.driver.get(url=self.URL)
        return self

    def wait_for_visible(self, locator, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator))

    def _get_element_locator_by_header_name(self, header):
        column_index = self.get_headers().index(header)
        locator = f"{self.__books_loc[1]}/div[{column_index + 1}]"
        return locator

    def get_name(self) -> str:
        return self.driver.find_element(*self.__store_name_loc).text

    def get_headers(self):
        locator = self.__headers_loc
        self.wait_for_visible(locator)
        return [
            header.text
            for header in self.driver.find_elements(*locator)
            if len(header.text) > 0]

    def get_header_button(self, name):
        locator = self.__headers_loc
        self.wait_for_visible(locator)
        return [header for header in self.driver.find_elements(*locator)
                if header.text == name][0]

    def get_header_elements(self, header_name: str):
        raise NotImplemented

    def get_publisher_names(self):
        raise NotImplemented

    def get_authors(self):
        raise NotImplemented

    def get_image_sources(self):
        locator = f'{self._get_element_locator_by_header_name("Image")}//img'
        elements = self.driver.find_elements(By.XPATH, locator)
        return [data.get_attribute('src') for data in elements]

    def get_publishers_for_author(self, author: str):
        raise NotImplemented

    def clear_search_field(self):
        raise NotImplemented

    def do_search(self, search_string: str):
        raise NotImplemented
