import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class', autouse=True)
def get_chrome():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument('--start-maximized')
    driver = Chrome(ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()
