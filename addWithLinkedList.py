import unittest


class Tests(unittest.TestCase):
    def test0(self):
        self.assertEqual([], arrayIntersection([], [1,2]))

    def test3(self):
        self.assertEqual([], arrayIntersection([1,2], []))

    def test1(self):
        self.assertEqual([2], arrayIntersection([1,2,3],[2,4]))

    def test2(self):
        self.assertEqual([1,2], arrayIntersection([1,2,3,1,2],[2,6,7,8,1]))

if __name__ == "__main__":
    unittest.main()
