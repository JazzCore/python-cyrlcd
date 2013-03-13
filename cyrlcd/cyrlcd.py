# -*- coding: utf-8 -*-

class CyrLCD(object):
    def __init__(self):
        self.letters = {
                u'а' : u'\\x61',
                u'б' : u'\\xb2',
                u'в' : u'\\xb3',
                u'г' : u'\\xb4',
                u'д' : u'\\xe3',
                u'е' : u'\\x65',
                u'ё' : u'\\x66',
                u'ж' : u'\\x67',
                u'з' : u'\\xb7',
                u'и' : u'\\xb8',
                u'й' : u'\\xb9',
                u'к' : u'\\xba',
                u'л' : u'\\xbb',
                u'м' : u'\\xbc',
                u'н' : u'\\xbd',
                u'о' : u'\\x6f',
                u'п' : u'\\xbe',
                u'р' : u'\\x70',
                u'с' : u'\\x63',
                u'т' : u'\\xbf',
                u'у' : u'\\x79',
                u'ф' : u'\\xe4',
                u'х' : u'\\x78',
                u'ч' : u'\\xc0',
                u'ц' : u'\\xe5',
                u'ш' : u'\\xc1',
                u'щ' : u'\\xe6',
                u'ъ' : u'\\xc2',
                u'ы' : u'\\xc3',
                u'ь' : u'\\xc4',
                u'э' : u'\\xc5',
                u'ю' : u'\\xc6',
                u'я' : u'\\xc7',
                u'А' : u'\\x41',
                u'Б' : u'\\xa0',
                u'В' : u'\\x42',
                u'Г' : u'\\xa1',
                u'Д' : u'\\xe0',
                u'Е' : u'\\x45',
                u'Ё' : u'\\xa2',
                u'Ж' : u'\\xa3',
                u'З' : u'\\xa4',
                u'И' : u'\\xa5',
                u'Й' : u'\\xa6',
                u'К' : u'\\x4b',
                u'Л' : u'\\xa7',
                u'М' : u'\\x4d',
                u'Н' : u'\\x48',
                u'О' : u'\\x4f',
                u'П' : u'\\xa7',
                u'Р' : u'\\x50',
                u'С' : u'\\x43',
                u'Т' : u'\\x54',
                u'У' : u'\\xa9',
                u'Ф' : u'\\xaa',
                u'Х' : u'\\x58',
                u'Ц' : u'\\xe1',
                u'Ч' : u'\\xab',
                u'Ш' : u'\\xac',
                u'Щ' : u'\\xe2',
                u'Ъ' : u'\\xad',
                u'Ы' : u'\\xae',
                u'Э' : u'\\xaf',
                u'Ю' : u'\\xb0',
                u'Я' : u'\\xb1',
                u' ' : u'\\x20',
                u'0' : u'\\x30',
                u'1' : u'\\x31',
                u'2' : u'\\x32',
                u'3' : u'\\x33',
                u'4' : u'\\x34',
                u'5' : u'\\x35',
                u'6' : u'\\x36',
                u'7' : u'\\x37',
                u'8' : u'\\x38',
                u'9' : u'\\x39',
                u'.' : u'\\x2e'
                }

    def conv(self, string):
        string = string.decode('utf-8')
        out = [self.letters[x] for x in string if x in self.letters]
        return ''.join(out)

    def convback(self, string):
        out = []
        for char in string:
            for item in self.letters.items():
                if int('0'+item[1][1:],16) == ord(char):
                    out.append(item[0])
            
        return ''.join(out)
