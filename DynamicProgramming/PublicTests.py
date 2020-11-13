import unittest
from solution import num_trees

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(2, num_trees(2))

    def test2(self):
        self.assertEqual(5, num_trees(3))

    def test3(self):
        self.assertEqual(14, num_trees(4))

    def test4(self):
       self.assertEqual(42, num_trees(5))
        

if __name__ == "__main__":
    unittest.main()
