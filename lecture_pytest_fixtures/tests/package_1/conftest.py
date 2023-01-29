import pytest


@pytest.fixture(scope='class', autouse=True)
def lecture_16_pac_1_fixture():
    print('\nFixture for each class with tests in package_1 START')
    yield
    print('\nFixture for each class with tests in package_1 END')
