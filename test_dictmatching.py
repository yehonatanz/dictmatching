import pytest
import dictmatching


@pytest.fixture
def d():
    return dict(a=3, b=7)


def test_dictmatching(d):
    from d import a, b
    assert a == 3
    assert b == 7
