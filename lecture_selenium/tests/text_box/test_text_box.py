import pytest

from .helper import scroll_to_element, wait_to_be_clickable
from .locators import loc_text_boxes, loc_result_table
from .data_for_test import fields_data


@pytest.mark.usefixtures('text_box')
class TestTextBoxParametrizeDifferentLocatorsExample:

    @pytest.fixture(scope='function')
    def refresh(self):
        self.driver.refresh()

    @pytest.mark.parametrize('locator', ['css', 'xpath'])
    def test_full_name(self, locator, refresh):
        field = self.driver.find_element(
            *loc_text_boxes.get(locator).get('full_name_input'))
        submit = self.driver.find_element(
            *loc_text_boxes.get(locator).get('submit_button'))

        field.send_keys(fields_data.get('full_name'))

        scroll_to_element(submit)
        wait_to_be_clickable(self.driver, submit, timeout=5).click()

        result_field = self.driver.find_element(
            *loc_result_table.get('full_name'))

        assert result_field.text.split(':')[1] == fields_data.get('full_name')


@pytest.mark.usefixtures('text_box')
class TestTextBox:
    _CSS = loc_text_boxes.get('css')
    INPUT_NAME_LOC = _CSS.get('full_name_input')
    INPUT_EMAIL_LOC = _CSS.get('email_input')
    INPUT_CURR_ADDR_LOC = _CSS.get('curr_addr_input')
    INPUT_PERM_ADDR_LOC = _CSS.get('full_name_input')
    BUTTON_SUBMIT_LOC = _CSS.get('submit_button')

    def test_full_name_field(self):
        field = self.driver.find_element(*self.INPUT_NAME_LOC)
        submit = self.driver.find_element(*self.BUTTON_SUBMIT_LOC)

        field.send_keys(fields_data.get('full_name'))

        scroll_to_element(submit)
        submit.click()

        result_field = self.driver.find_element(
            *loc_result_table.get('full_name'))

        assert result_field.text.split(':')[1] == fields_data.get('full_name')

    def test_email_field_valid(self):
        email = fields_data.get('email').get('valid')
        field = self.driver.find_element(*self.INPUT_EMAIL_LOC)
        submit = self.driver.find_element(*self.BUTTON_SUBMIT_LOC)

        field.send_keys(email)

        scroll_to_element(submit)
        submit.click()

        result_field = self.driver.find_element(
            *loc_result_table.get('email'))

        result_text = result_field.text.split(':')[1]
        assert result_text == email

    def test_email_field_invalid(self):
        self.driver.refresh()
        email = fields_data.get('email').get('invalid')
        field = self.driver.find_element(*self.INPUT_EMAIL_LOC)
        submit = self.driver.find_element(*self.BUTTON_SUBMIT_LOC)

        field.send_keys(email)

        scroll_to_element(submit)
        submit.click()

        assert 'error' in field.get_attribute('class')

    def test_curr_addr_field(self):
        self.driver.refresh()
        field = self.driver.find_element(*self.INPUT_CURR_ADDR_LOC)
        submit = self.driver.find_element(*self.BUTTON_SUBMIT_LOC)

        addr = fields_data.get('curr_addr')
        field.send_keys(addr)

        scroll_to_element(submit)
        submit.click()

        result_field = self.driver.find_element(
            *loc_result_table.get('curr_addr'))

        result_text = result_field.text.split(':')[1]
        assert addr == result_text
