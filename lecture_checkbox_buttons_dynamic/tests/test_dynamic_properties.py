from _pytest.python_api import raises
from selenium.common import InvalidElementStateException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lecture_checkbox_buttons_dynamic.tests.helper import is_element_enabled


class TestDynamicProperties:

    def test_get_id(self, dynamic_properties, get_element_id):
        element = dynamic_properties.find_element(By.ID, get_element_id)
        assert 'random' in element.text

    def test_wait_for_enable_element(self, dynamic_properties):
        locator = (By.CSS_SELECTOR, '#enableAfter')
        WebDriverWait(driver=dynamic_properties, timeout=6).until(
            expected_conditions.element_to_be_clickable(locator))
        el = dynamic_properties.find_element(*locator)
        assert el.is_enabled()

    def test_custom_method_check_if_element_enabled(self, dynamic_properties):
        locator = (By.CSS_SELECTOR, '#enableAfter')
        assert is_element_enabled(dynamic_properties, locator, 6)

    def test2_custom_method_check_if_element_enabled(self, dynamic_properties):
        """
        If timeout is less than 5, is_element_enabled() method
        should return exception: InvalidElementStateException
        (element is present, but not enabled)
        """
        locator = (By.CSS_SELECTOR, '#enableAfter')
        with raises(InvalidElementStateException):
            assert is_element_enabled(dynamic_properties, locator, 1)

    def test_button_is_present(self, dynamic_properties):
        dynamic_properties.refresh()
        locator = (By.CSS_SELECTOR, "#visibleAfter")
        WebDriverWait(driver=dynamic_properties, timeout=5.5).until(
            expected_conditions.visibility_of_element_located(locator))
        assert dynamic_properties.find_element(*locator).is_displayed()
