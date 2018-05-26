dictmatching
=============
.. image:: https://travis-ci.com/yehonatanz/dictmatching.svg?branch=master
    :target: https://travis-ci.com/yehonatanz/dictmatching
.. image:: https://codecov.io/gh/yehonatanz/dictmatching/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/yehonatanz/dictmatching

Unpacking dicts is now easier than ever:

.. code-block:: python
    
    from dictmatching import unpack
    
    d1 = dict(a=1, b=2)
    d2 = dict(x=3, y=4)
    with unpack(d1) as b, unpack(d2) as (x, y):
        assert b == 2
        assert x == 3
        assert y == 4
