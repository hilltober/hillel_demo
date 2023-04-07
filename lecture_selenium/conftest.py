import pytest
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope='class')
def chrome(request):
    driver: WebDriver = request.getfixturevalue("demoqa")
    driver.implicitly_wait(4)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
