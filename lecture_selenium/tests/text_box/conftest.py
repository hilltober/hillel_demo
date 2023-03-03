import pytest


@pytest.fixture(scope='class')
def text_box(request):
    driver = request.getfixturevalue("set_browser_for_demoqa")
    driver.get('https://demoqa.com/text-box')

    if request.cls:
        request.cls.driver = driver

    yield driver
    driver.quit()
