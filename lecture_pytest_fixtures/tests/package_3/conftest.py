import pytest


@pytest.fixture(scope='package', autouse=True)
def pac3_fixture():
    print('\n fixture for package_3 START')
    yield
    print('\n fixture for package_3 END')
