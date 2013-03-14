Python-CyrLCD: Convert strings to HD44780 compatible string
===========================================================

Python module to convert cyrillic strings to "\\xFF"-like format and vice versa.

Usage
-----

.. code-block:: python

    >>> import cyrlcd

    >>> print cyrlcd.str2hex("Проверка связи")
    \xa7\x70\x6f\xb3\x65\x70\xba\x61\x20\x63\xb3\xc7\xb7\xb8

    >>> print cyrlcd.hex2str('\xa7\x70\x6f\xb3\x65\x70\xba\x61\x20\x63\xb3\xc7\xb7\xb8')
    Проверка связи
