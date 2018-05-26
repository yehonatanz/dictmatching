import pytest

from dictmatching import unpack


@pytest.fixture
def d():
    return dict(a=3, b=7)


def test_unpack_one(d):
    with unpack(d) as a:
        assert a == 3


def test_unpack_multi(d):
    with unpack(d) as (a, b):
        assert a == 3
        assert b == 7


def test_unpack_multi_single(d):
    with unpack(d) as (b,):
        assert b == 7


def test_unpack_multiline(d):
    with unpack(d) as (
        a,
        b,
    ):
        assert a == 3
        assert b == 7
