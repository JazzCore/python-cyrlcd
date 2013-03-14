import unittest
import os
import sys

#Prepend ../ to PYTHONPATH so that we can import cyrlcd form there.
TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.realpath(os.path.join(TESTS_ROOT, '..')))

import cyrlcd

class TestCyrLCD(unittest.TestCase):
    
    def test_str2hex(self):
        r  = cyrlcd.str2hex("Проверка")
        self.assertEqual(r,u'\\xa7\\x70\\x6f\\xb3\\x65\\x70\\xba\\x61')

    def test_hex2str(self):
        r = cyrlcd.hex2str(u'\\xa7\\x70\\x6f\\xb3\\x65\\x70\\xba\\x61')
        self.assertEqual(r, u'\u0445\u04307\u044570\u04456\u0451\u04453\u044565\u044570\u0445\u0430\u044561')
