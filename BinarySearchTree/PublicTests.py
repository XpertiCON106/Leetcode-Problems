import unittest
from solution import is_bst

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertTrue(is_bst((i for i in [10, 5, 15])))

    def test2(self):
        self.assertFalse(is_bst((i for i in [10, 15, 25])))

    def test3(self):
        self.assertFalse(is_bst((i for i in [6, 3, 2])))

    def test4(self):
       self.assertFalse(is_bst((i for i in [50, 37, 68, 20, 40, 70, None])))
        

if __name__ == "__main__":
    unittest.main()
