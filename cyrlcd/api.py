# -*- coding: utf-8 -*-

from .cyrlcd import CyrLCD

def str2hex(string):
    r = CyrLCD()
    return r.conv(string)

def hex2str(string):
    r = CyrLCD()
    return r.convback(string)
