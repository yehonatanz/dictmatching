dictmatching
=============
.. image:: https://travis-ci.com/yehonatanz/dictmatching.svg?branch=master
    :target: https://travis-ci.com/yehonatanz/dictmatching
.. image:: https://codecov.io/gh/yehonatanz/dictmatching/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/yehonatanz/dictmatching

Unpacking dicts is now easier than ever:

.. code-block:: python
    
    from dictmatching import unpack
    
    d = {'a': 3, 'b': 7}
    with unpack(d) as (a, b):
        print('{} + {} = {}'.format(a, b, a + b))
