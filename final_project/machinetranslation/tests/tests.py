import unittest

from translator import english_to_french
from translator import french_to_english

class Test(unittest.TestCase):
    def test_e(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'), '')
        self.assertNotEqual(english_to_french(0), 0)
    
    def test_f(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('None'), '')
        self.assertNotEqual(french_to_english(0), 0)

if __name__=='__main__':
    unittest.main()