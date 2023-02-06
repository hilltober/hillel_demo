import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def checkboxes(request):
    driver = request.getfixturevalue("get_chrome")
    driver.get('https://demoqa.com/checkbox')
    yield driver


@pytest.fixture(scope='class')
def radio_buttons(request):
    driver = request.getfixturevalue("get_chrome")
    driver.get('https://demoqa.com/radio-button')
    yield driver


@pytest.fixture(scope='class')
def dynamic_properties(request):
    driver = request.getfixturevalue("get_chrome")
    driver.get('https://demoqa.com/dynamic-properties')
    yield driver


@pytest.fixture(scope='function')
def get_element_id(request):
    driver = request.getfixturevalue("dynamic_properties")
    element = driver.find_element(By.XPATH,
                                  '//p[text()="This text has random Id"]')
    yield element.get_attribute('id')


@pytest.fixture(scope='function', autouse=True)
def refresh_page(request):
    driver = request.getfixturevalue("get_chrome")
    yield
    driver.refresh()
