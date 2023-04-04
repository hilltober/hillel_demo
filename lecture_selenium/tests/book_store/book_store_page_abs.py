from abc import abstractmethod, ABC


class BookStorePage(ABC):

    @abstractmethod
    def _get_element_locator_by_header_name(self, header_name: str):
        raise NotImplementedException

    @abstractmethod
    def open(self):
        raise NotImplementedException

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_headers(self):
        raise NotImplementedException

    @abstractmethod
    def get_header_button(self, mame: str):
        raise NotImplementedException

    @abstractmethod
    def get_header_elements(self, header_name: str):
        raise NotImplementedException

    @abstractmethod
    def get_publisher_names(self):
        raise NotImplementedException

    @abstractmethod
    def get_authors(self):
        raise NotImplementedException

    @abstractmethod
    def get_image_sources(self):
        raise NotImplementedException

    @abstractmethod
    def get_publishers_for_author(self, author: str):
        raise NotImplementedException

    @abstractmethod
    def clear_search_field(self):
        raise NotImplementedException

    @abstractmethod
    def do_search(self, search_string: str):
        raise NotImplementedException
