import pytest


@pytest.fixture(scope='function', autouse=True)
def package_2_fixture_for_each_test():
    print('\nPackage 2 fixture for each test START')
    yield
    print('\nPackage 2 fixture for each test END')
