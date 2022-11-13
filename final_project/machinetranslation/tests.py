import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
    def test2(self):
        self.assertEqual(english_to_french(None),"Insert data")
    def test3(self):
        self.assertNotEqual(english_to_french(None),None)

class testFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    def test2(self):
        self.assertEqual(french_to_english(None),"Insert data")
    def test3(self):
        self.assertNotEqual(french_to_english(None),None)

unittest.main()