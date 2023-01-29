import pytest


@pytest.fixture(scope='package', autouse=True)
def lecture_16_fixture():
    print('\nOutside packages (global, scope=package) fixture START')
    yield
    print('\nOutside packages (global, scope=package) fixture END')
