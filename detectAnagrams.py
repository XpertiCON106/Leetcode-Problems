import unittest
"""
Question:
Given two strings t and s determine if they are anagrams of each other.
Anagrams are two strings that use the exact same characters.
For example “angered” and “enraged” are anagrams of each other.
However, you cannot use hashing, i.e. no hash tables or hash sets or
hash maps are allowed.

Examples:
“angered”, “enraged” → true
“salad”, “dallas” → false
================================================================================
for this problem, i decided to implement mergesort to sort the first two arrays
I then compared if both are equal. If equal, then return true, which means
it is an anagram. If not then, return false, which is not an anagram.

for the mergesort function, i take in an array.
i divide the array in the middle, L and R array.
then i mergeSort both of those.

then i have two counters that checks through array L and array R

I basically check through 1 by 1. if L[i] < R[j], i put L[i] in the resulting
array. Increment i. if L[i] > R[j], put in R[j] and increment j. I do this
until both arrays are exhausted.

One challenge i had was prematurally ending the merge. This happened when both
strings are not of equal length. To rememdy this, i make sure, whatever elements
are left of either array, i fill them back in the resulting array.

Because mergesort is stable, the relative ordering of the elements are
presereved, So i don't have to worry about any re sorting issues.

So, sorting first array takes O(log n)
sorting the second takes O(log n)

and we just do a comparison check at the end so, overall O(log n) algorithm
"""
def are_anagrams(t,s):
    if len(t) != len(s):
        print("Not an anagram")
        return False

    arr1 = [x for x in t]
    arr2 = [x for x in s]

    mergeSort(arr1)
    mergeSort(arr2)

    if arr1 == arr2:
        print("Is an anagram")
        return True

    print("Not an anagram")
    return False


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
