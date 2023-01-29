import pytest


@pytest.mark.param
@pytest.mark.parametrize('single_val', [2, 4, 6])
def test_param_1(single_val):
    assert single_val % 2 == 0


@pytest.mark.param
@pytest.mark.parametrize('k,v', [(1, 1), (2, 2), (3, 3)])
def test_param_2(k, v):
    assert k == v


@pytest.mark.param
@pytest.mark.parametrize('val, _type',
                         [(1, int), (2.0, float), (True, bool)],
                         ids=['integer', 'float', 'boolean'])
def test_param_2(val, _type):
    assert type(val) is _type
