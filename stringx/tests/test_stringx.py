import unittest
from stringx.stringx import *


class TestStringx(unittest.TestCase):

    def test_is_number(self):
        self.assertEqual(is_number(''), False)
        self.assertEqual(is_number('1970'), True)
        self.assertEqual(is_number(1970), True)
        self.assertEqual(is_number('2am'), False)
        self.assertEqual(is_number('a'), False)
        self.assertEqual(is_number('NaN'), False)
        self.assertEqual(is_number('nan'), False)
        self.assertEqual(is_number('1'), True)
        self.assertEqual(is_number('-1'), True)
        self.assertEqual(is_number('1.1'), True)
        self.assertEqual(is_number('-1.1'), True)

    def test_to_ascii_str(self):
        self.assertEqual(to_ascii_str('abcdefghijklmnopqrstuvwxyz'), 'abcdefghijklmnopqrstuvwxyz')
        aa_map = {
            'À': 'A',
            'Á': 'A',
            'Â': 'A',
            'Ã': 'A',
            'Ä': 'A',
            'Ç': 'C',
            'È': 'E',
            'É': 'E',
            'Ê': 'E',
            'Ë': 'E',
            'Ì': 'I',
            'Í': 'I',
            'Î': 'I',
            'Ï': 'I',
            'Ñ': 'N',
            'Ò': 'O',
            'Ó': 'O',
            'Ô': 'O',
            'Õ': 'O',
            'Ö': 'O',
            'Š': 'S',
            'Ú': 'U',
            'Û': 'U',
            'Ü': 'U',
            'Ù': 'U',
            'Ý': 'Y',
            'Ÿ': 'Y',
            'Ž': 'Z',
            'à': 'a',
            'á': 'a',
            'â': 'a',
            'ã': 'a',
            'ä': 'a',
            'ç': 'c',
            'è': 'e',
            'é': 'e',
            'ê': 'e',
            'ë': 'e',
            'ì': 'i',
            'í': 'i',
            'î': 'i',
            'ï': 'i',
            'ñ': 'n',
            'ò': 'o',
            'ó': 'o',
            'ô': 'o',
            'õ': 'o',
            'ö': 'o',
            'š': 's',
            'ù': 'u',
            'ú': 'u',
            'û': 'u',
            'ü': 'u',
            'ý': 'y',
            'ÿ': 'y',
            'ž': 'z'
        }
        for k, v in aa_map.items():
            self.assertEqual(to_ascii_str(k), v)


if __name__ == '__main__':
    unittest.main()
