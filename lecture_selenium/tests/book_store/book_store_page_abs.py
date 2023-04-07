from abc import abstractmethod, ABC


class BookStorePage(ABC):

    @abstractmethod
    def _get_element_locator_by_header_name(self, header_name: str):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_headers(self):
        pass

    @abstractmethod
    def get_header_button(self, mame: str):
        pass

    @abstractmethod
    def get_header_elements(self, header_name: str):
        pass

    @abstractmethod
    def get_publisher_names(self):
        pass

    @abstractmethod
    def get_authors(self):
        pass

    @abstractmethod
    def get_image_sources(self):
        pass

    @abstractmethod
    def get_publishers_for_author(self, author: str):
        pass

    @abstractmethod
    def clear_search_field(self):
        pass

    @abstractmethod
    def do_search(self, search_string: str):
        pass
