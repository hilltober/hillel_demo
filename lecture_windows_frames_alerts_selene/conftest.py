import pytest
from selene.support.shared import config
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class', name='headless_firefox')
def setup_headless_firefox():
    options = Options()
    options.headless = True
    driver = Firefox(
        executable_path=GeckoDriverManager().install(),
        options=options)
    config.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='class', name='qa')
def set_base_page():
    config.base_url = 'https://demoqa.com/'
