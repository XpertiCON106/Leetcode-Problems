import unittest

class LinkedNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def add_linked_lists(list1, list2):
    prev = None
        temp = None
        carry = 0

        # While both list exists
        while(first is not None or second is not None):
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata

            # update carry for next calculation
            carry = 1 if Sum >= 10 else 0

            # update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10

            # Create a new node with sum as data
            temp = Node(Sum)

            # if this is the first node then set it as head
            # of resultant list
            if self.head is None:
                self.head = temp
            else :
                prev.next = temp

            # Set prev for next insertion
            prev = temp

            # Move first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)
        return list1

class Tests(unittest.TestCase):

    def test0(self):
        list1 = LinkedNode(5, (LinkedNode(3, (LinkedNode(7, None)))))
        list2 = LinkedNode(1, (LinkedNode(2, (LinkedNode(2, None)))))

        result = LinkedNode(9, (LinkedNode(5, (LinkedNode(6, None)))))
        self.assertEqual(result, add_linked_lists(list1, list2))


if __name__ == "__main__":
    unittest.main()
