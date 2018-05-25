import pytest

from dictmatching import unpack


@pytest.fixture
def d():
    return dict(a=3, b=7)


def test_unpack_one(d):
    with unpack(d) as a:
        assert a == 3
    assert a == 3
