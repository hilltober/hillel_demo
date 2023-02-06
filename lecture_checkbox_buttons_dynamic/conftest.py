import pytest
from selenium import webdriver
from selenium.webdriver import Chrome


@pytest.fixture(scope='class', autouse=True)
def get_chrome():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = Chrome(executable_path='D:\\Drivers\\chromedriver.exe',
                    options=options)
    yield driver
    driver.quit()
