import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def text_box(request):
    options = webdriver.ChromeOptions()
    options.headless = True

    driver = Chrome(executable_path=ChromeDriverManager().install(),
                    options=options)
    driver.get('https://demoqa.com/text-box')

    if request.cls:
        request.cls.driver = driver

    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def chrome():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def chrome_headless():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = Chrome(options=chrome_options)
    yield driver
    driver.quit()
