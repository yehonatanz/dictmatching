import pytest

from dictmatching import unpack


@pytest.fixture
def d():
    return dict(a=3, b=7)


@pytest.fixture
def other(d):
    return dict({k: -v for k, v in d.items()}, c=True)


def test_unpack_one(d):
    with unpack(d) as a:
        assert a == 3


def test_unpack_non_existent(d):
    with pytest.raises(KeyError):
        with unpack(d) as non_existent:
            pass


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


def test_unpack_several_dicts(d, other):
    with unpack(d) as a, unpack(other) as (b, a):
        assert a == -3
        assert b == -7
    with unpack(d) as (a, b), unpack(other) as b:
        assert a == 3
        assert b == -7
    with unpack(d) as a, unpack(other) as c:
        assert a == 3
        assert c is True


def test_unpack_several_dict_no_mix(d, other):
    with pytest.raises(KeyError):
        with unpack(d) as (a, c), unpack(other) as (a, c):
            pass
