# The rotation of a linked list can be defined as an operation that makes a node k
# the new head of the linked list, and appends each element that was before k to the
# end of the linked list. We can call the element selected the kth element of the linked
# list, and thus call the resulting linked list the kth rotation.

# Write a function, which takes a Node and an integer k as it’s arguments and returns a new
# node that is the head of the kth rotation of the linked list. If the value k is longer than
# the length of the linked list, is 0, or is negative, instead return the original linked list.
# If the Node is None, return None. You will not be passed a circular linked list.
# You are guaranteed the linked list will have no more than 1,000,000 nodes.

from Node import Node

def rotate_list(head: 'Node', k: int) -> 'Node':
    # if k == 0 or less then 0, return the head
    if(k == 0 or k < 0):
        return head

    # Now we know k is valid and we can continue with rotation
    head, child = traverse(head,None, k, 0)
    if(child == None):
        return head
    insert(child, head)
    head = child
    return head

def insert(head: 'Node', insertThis: 'Node'):
    if(head.next != None):
        insert(head.next, insertThis)
    else:
        head.next = insertThis

def traverse(head: 'Node',child: 'None', k: int, index: int) -> ('Node', 'Node'):
    if(index > k):
        return head, None

    if(head != None):
        if(index == k):
            child = head
            head = None
        else:
            index+=1
            head.next, child = traverse(head.next,child,k, index)

    return head, child
    # TODO
