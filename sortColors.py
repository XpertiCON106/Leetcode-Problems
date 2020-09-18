import unittest
"""
Problem
Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red,
 white, and blue respectively.

 Your function should sort the array in place, and should not return anything.

Note: You are not supposed to use the library's sort function for this problem.

Follow up: Can you do this with one pass?

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""

"""
For this problem i decided to implement a hash. Basically I go through the array
once and keeping in track of the number of times 0,1, or 2 appears. The insertion
and search takes O(1) time since its a hash table.

Then I append 0, 1, or 2 on the array based on how many times it appears in the
hash. So it will take O(n) since we have to add N many times to the array.

Overall, time complexity of O(n). And space complexity of O(n) as well because of the
hash table.

I did not have any issues/challenge with this problem. 
"""
def sortColor(arr):
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1

    print(dict)
    arr.clear()
    arr.append([0] * dict[0])
    arr.append([1] * dict[1])
    arr.append([2] * dict[2])

    return arr

class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test0(self):
        self.assertEqual([0,0,1,1,2,2], sortColor([2,0,2,1,1,0]))

if __name__ == "__main__":
    unittest.main()
