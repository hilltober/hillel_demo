import time
import pytest


@pytest.mark.timed
def test_0():
    assert False


@pytest.mark.timed
def test_1():
    time.sleep(1)
    pass


@pytest.mark.timed
def test_2():
    time.sleep(1)
    pass


@pytest.mark.timed
def test_3():
    time.sleep(1)
    pass


@pytest.mark.timed
def test_4():
    time.sleep(1)
    pass


@pytest.mark.timed
def test_5():
    time.sleep(1)
    pass


@pytest.mark.timed
def test_6():
    time.sleep(12)
    pass
