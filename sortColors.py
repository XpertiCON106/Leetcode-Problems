import unittest

def sortColor(arr):
    return arr

class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test0(self):
        self.assertEqual([0,0,1,1,2,23], sortColor([2,0,2,1,1,0]))

if __name__ == "__main__":
    unittest.main()
