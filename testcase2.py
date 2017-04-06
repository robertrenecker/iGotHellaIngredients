import unittest

class AlphaTest(unittest.TestCase):
    def test_1(self):
        ingredients = ['Egg']
        self.assertEqual(search(ingredients), "Egg is in Fried Rice\n")
