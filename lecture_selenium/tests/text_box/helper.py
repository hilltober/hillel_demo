from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def scroll_to_element(element: WebElement) -> None:
    _ = element.location_once_scrolled_into_view


def wait_to_be_clickable(driver, element: WebElement, timeout=1) -> WebElement:
    WebDriverWait(driver=driver, timeout=timeout).until(
        expected_conditions.element_to_be_clickable(element))
    return element
