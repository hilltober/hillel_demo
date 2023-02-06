import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='class')
def text_box(request):
    driver = Chrome(executable_path='D:\\Drivers\\chromedriver.exe')
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
