from selenium.webdriver.common.by import By

from lecture_checkbox_buttons_dynamic.tests.helper import select_folders, \
    expand_full_tree, optimize_test_data, expand_folders, \
    select_folder


class TestCheckboxes:

    def test_checkboxes(self, checkboxes):
        driver = checkboxes
        folders = ['Commands', 'General', 'Private']
        expand_full_tree(driver)
        select_folders(driver, optimize_test_data(folders).get('tree'))
        result = driver.find_element(
            By.CSS_SELECTOR, 'div#result').text.split(':')[1].split()
        assert sorted(result) == sorted(
            optimize_test_data(folders).get('results'))

    def test_checkboxes_bonus(self, checkboxes):
        driver = checkboxes
        folders = ['Home', 'Documents', 'Office']
        target_folder = 'General'
        expand_folders(driver, folders)
        select_folder(driver, target_folder)
        result = driver.find_element(
            By.CSS_SELECTOR, 'div#result').text.split(':')[1].split()
        assert all([len(result) == 1, target_folder.lower() == result[0]])
