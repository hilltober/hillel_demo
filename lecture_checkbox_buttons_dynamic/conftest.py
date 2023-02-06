import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='class', autouse=True)
def get_chrome():
    driver = Chrome(executable_path='D:\\Drivers\\chromedriver.exe')
    yield driver
    driver.quit()
