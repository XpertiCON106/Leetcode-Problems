import unittest
from solution import commonElements

class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(true, are_anagrams("angered", "enraged"))

    def test2(self):
        self.assertEqual(false, are_anagrams("salad", "dallas"))

if __name__ == "__main__":
    unittest.main()
