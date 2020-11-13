import unittest
from solution import is_bipartite

class PublicTests(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertTrue(is_bipartite([[1,3],[0,2],[1,3],[0,2]]))

    def test2(self):
        self.assertFalse(is_bipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))

    def test3(self):
        self.assertFalse(is_bipartite([[1,2],[0,2],[0,1]]))

    def test4(self):
        self.assertTrue(is_bipartite([[], [], []]))


if __name__ == "__main__":
    unittest.main()
