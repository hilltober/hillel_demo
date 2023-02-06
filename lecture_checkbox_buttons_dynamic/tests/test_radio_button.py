from selenium.webdriver.common.by import By


class TestCheckboxes:

    def test_activate_yes_radio(self, radio_buttons):
        driver = radio_buttons
        input_yes = driver.find_element(By.CSS_SELECTOR, '#yesRadio')
        label_yes = driver.find_element(By.CSS_SELECTOR, '[for="yesRadio"]')
        label_yes.click()
        is_input_selected = input_yes.is_selected()
        result_text = driver.find_element(
            By.CSS_SELECTOR, 'span.text-success').text
        assert all([is_input_selected, result_text == 'Yes'])

    def test_get_radio_buttons_info(self, radio_buttons):
        driver = radio_buttons
        inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
        labels = driver.find_elements(By.CSS_SELECTOR, 'label[for]')
        labels[0].click()
        labels = [label.text for label in labels]
        states = [state.is_selected() for state in inputs]
        result_dict = dict(zip(labels, states))
        assert result_dict.get('Yes')

    def test_activate_disabled_radio_button(self, radio_buttons):
        driver = radio_buttons
        input_no = driver.find_element(By.CSS_SELECTOR, '#noRadio')
        label_no = driver.find_element(By.CSS_SELECTOR, '[for="noRadio"]')
        driver.execute_script(
            "arguments[0].removeAttribute('disabled','disabled')", input_no)
        label_no.click()
        is_input_selected = input_no.is_selected()
        assert is_input_selected
