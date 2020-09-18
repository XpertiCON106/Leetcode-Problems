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

"""
I approach this problem by first sorting both the arrays using merge sort.
That will take O(n Log n). Then i go by each array one indexes at a time.
If both values are equal, add it to the resulting array.
While comparing, increase the indexes of the smaller element. That way we are
checking all the elements while making sure we're not running out of elements.
Only increase both the indexes if elements are equal.
So time complexity is O(n log n) to sort the array. and O(n) to go through
both the array.

One challege Im currently having is infinite loop. I fixed this by having an
additional check that sees if either of the indexes reach the length of
their respective arrays, end the loop.
"""
def arrayIntersection(arr1, arr2):
    if len(arr1) == 0:
        return arr1

    if len(arr2) == 0:
        return arr2

    mergeSort(arr1)
    mergeSort(arr2)

    res = []
    i = j = 0
    bool = False
    while True:
        if i < len(arr1):
            a = arr1[i]

        if j < len(arr2):
            b = arr2[j]

        if a == b and a not in res:
            res.append(a)
            i+=1
            j+=1

        if a < b:
            i+=1

        if i == len(arr1) or j == len(arr2):
            break

    return res

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1

        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1

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
