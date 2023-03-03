import pytest


@pytest.fixture(scope='class', autouse=True)
def get_chrome(request):
    driver = request.getfixturevalue("set_browser_for_demoqa")
    yield driver
    driver.quit()
