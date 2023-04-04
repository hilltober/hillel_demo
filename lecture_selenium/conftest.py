import pytest


@pytest.fixture(scope='class')
def chrome(request):
    driver = request.getfixturevalue("demoqa")
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
