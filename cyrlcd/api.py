# -*- coding: utf-8 -*-

from .cyrlcd import CyrLCD

def str2hex(string):
    """
    Convert string to a hex format, "\\xFF" style.

    :param string: string to convert
    """
    r = CyrLCD()
    return r.conv(string)

def hex2str(string):
    """
    Convert hex string in "\xFF" format to a normal string.

    :param string: string to convert
    """
    r = CyrLCD()
    return r.convback(string)
