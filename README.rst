m26 - calculations for sports like running, cycling, and swimming
=================================================================

Features
--------

- Specify distances in either miles, kilometers, or yards.
- Translates distances to the other units of measure.
- Specify elapsed times either in 'hh:mm:ss' strings, or int second values.
- Calculates speed - per mile, per kilometer, or per yard.
- Calculates pace - per mile.
- Projects one speed to another distance with either simple or algorithmic formulas.
- Calculates age of person, and age-graded times.
- Calculates heart-rate training zones based on age.


Quick start
-----------

Installation:

.. code-block:: console

    $ pip install m26

Use:

.. code-block:: pycon

    >>> import m26
    >>> from m26.age import Age
    >>> from m26.age_calculator import AgeCalculator
    >>> from m26.constants import Constants
    >>> from m26.distance import Distance
    >>> from m26.elapsed_time import ElapsedTime
    >>> from m26.run_walk_calculator import RunWalkCalculator
    >>> from m26.speed import Speed

    >>> d1 = Distance(26.2)
    >>> d2 = Distance(50.0, 'k')


Source Code
-----------

See `m26-py at GitHub <https://github.com/cjoakim/m26-py>`_ .
