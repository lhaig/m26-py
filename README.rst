m26 - calculations for sports like running, cycling, and swimming
=================================================================

Features
--------

- Specify distances in either miles, kilometers, or yards.
- Specify elapsed times either in 'hh:mm:ss' strings, or int second values.
- Calculates speed - per mile, per kilometer, or per yard.
- Calculates pace - per mile.
-
- Translates

Quick start
-----------

Installation:

.. code-block:: console

    $ pip install m26

And then:

.. code-block:: pycon

    >>> import arrow
    >>> utc = arrow.utcnow()
    >>> utc
    <Arrow [2013-05-11T21:23:58.970460+00:00]>

    >>> utc = utc.replace(hours=-1)
    >>> utc
    <Arrow [2013-05-11T20:23:58.970460+00:00]>

    >>> local = utc.to('US/Pacific')
    >>> local
    <Arrow [2013-05-11T13:23:58.970460-07:00]>

    >>> arrow.get('2013-05-11T21:23:58.970460+00:00')
    <Arrow [2013-05-11T21:23:58.970460+00:00]>

    >>> local.timestamp
    1368303838

    >>> local.format()
    '2013-05-11 13:23:58 -07:00'

    >>> local.format('YYYY-MM-DD HH:mm:ss ZZ')
    '2013-05-11 13:23:58 -07:00'

    >>> local.humanize()
    'an hour ago'

    >>> local.humanize(locale='ko_kr')
    '1시간 전'

Further documentation can be found at `arrow.readthedocs.org <http://arrow.readthedocs.org/en/latest/>`_

Contributing
------------

Contributions are welcome, especially with localization.  See `locales.py <https://github.com/crsmithdev/arrow/blob/master/arrow/locales.py>`_ for what's currently supported.
