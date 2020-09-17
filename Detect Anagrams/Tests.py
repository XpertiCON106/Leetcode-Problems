import unittest
from detectAnagrams import are_anagrams

class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test0(self):
        self.assertEqual(False, are_anagrams("1", "bruh"))

    def test1(self):
        self.assertEqual(True, are_anagrams("angered", "enraged"))

    def test2(self):
        self.assertEqual(False, are_anagrams("salad", "dallas"))


if __name__ == "__main__":
    unittest.main()
