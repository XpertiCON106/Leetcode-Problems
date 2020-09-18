import unittest
"""
Given two arrays A and B, compute their intersection which is defined as all
numbers that exist in both A and B. Each number in the resulting intersection
must be unique, i.e. no duplicates. The intersection does not have to be in any
 specific order. However you cannot use hashing, i.e. no hash tables or hash
 sets or hash maps are allowed.
Clarification: you can only assume that keys are comparable
-- only <, >, <=, >=, and == are allowed. (only comparison based methods work)

"""

def arrayIntersection(arr1, arr2):
    return arr1

class Tests(unittest.TestCase):
    def test0(self):
        self.assertEqual([], arrayIntersection([], [1,2]))

    def test1(self):
        self.assertEqual([2], arrayIntersection([1,2,3],[2,4]))

    def test2(self):
        self.assertEqual([1,2], arrayIntersection([1,2,3,1,2],[2,6,7,8,1]))

if __name__ == "__main__":
    unittest.main()
