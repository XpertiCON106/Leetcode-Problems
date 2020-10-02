# The rotation of a linked list can be defined as an operation that makes a node k
# the new head of the linked list, and appends each element that was before k to the
# end of the linked list. We can call the element selected the kth element of the linked
# list, and thus call the resulting linked list the kth rotation.

# Write a function, which takes a Node and an integer k as it’s arguments and returns a new
# node that is the head of the kth rotation of the linked list. If the value k is longer than
# the length of the linked list, is 0, or is negative, instead return the original linked list.
# If the Node is None, return None. You will not be passed a circular linked list.
# You are guaranteed the linked list will have no more than 1,000,000 nodes.

"""
Name: Immamul Morsilin
UID: 114796103

We will use this linked list as a referece to explain my algorithm
0->1->2->3->4->5

The number is just the index, not the actual value of the nodes.

So, first we take care of the edge cases; if k == 0 or negative, just return the linked list

So if we have the linked list above, and k was 3. We know that our resulting list would linked

3->4->5->0->1->2

Here we can see, we actually have two linked list stiched together
Linked List 1: 3->4->5
Linked List 2: 0->1->2

My goal was to find these two linked list and stich them together.
To do that, I start traversing the linked list.

if we find the kth term, in this case 3, i have a child node that will be equal
to that node. So child node in this case will be 3, which follows with 4 and 5.
so the resulting linked list will be 3->4->5.

if we don't find the kth term, we go to the next node recursively and we keep check
of the head node.

once we find the kth term, we set child node equal to the kth node, and we set kth node
equal to None which makes everything from the k to len(head) node equal to None.
So the head node, in this case, becomes 0->1->2.

My recursive function returns a tuple (head, child) so after traversing in this cases
we will get the following.
child: 3->4->5
head: 0->1->2

so now we just need to add head node to the end of child node.

I use an insert method that traverses the child node until its at the last node.
then it just inserts it in.

the space complexity is O(n) because i have a child node that contains a portion of the linked list.

The time complexity is O(n) as well because first I traverse the linked list to find the kth value.
Once I find the kth value, I don't traverse it anymore. Then the i traverse from the kth node to the end
of the linked list of the child node to stich both of the linked list together. so basically traversing
through the rest of the list. So traversing through the entire linked list ONCE.

Because python has a recursion limit, i am unable to pass test 5 :(

"""
from Node import Node

def rotate_list(head: 'Node', k: int) -> 'Node':
    # if k == 0 or less then 0, return the head
    if(k == 0 or k < 0):
        return head

    # Now we know k is valid and we can continue with rotation

    # traverse the array until we find the kth value
    head, child = traverse(head,None, k, 0)

    # if child was returned null, that means we either did not find the kth value
    # or the index went beyond the size of the linked list. so we just return
    # the head
    if(child == None):
        return head

    # now we insert the head, which is the list from the head node upto and including
    # the kth nodes PARENT, to the child node, which is the kth node and any nodes that follow
    insert(child, head)

    # now we simply set head equals to child and return
    head = child
    return head

def insert(head: 'Node', insertThis: 'Node'):
    if(head.next != None):
        insert(head.next, insertThis)
    else:
        head.next = insertThis

def traverse(head: 'Node',child: 'None', k: int, index: int) -> ('Node', 'Node'):
    # head is what we traverse
    # child is what we set to after we find the kth node
    # index just tracks how many nodes we went through

    # if index > k, we just return the head and the child which will be none cause we
    # didn't find any, index went overboard.
    if(index > k):
        return head, None

    # if this head exists
    if(head != None):
        # if we find the kth value
        if(index == k):
            # we set child equal to this head and any nodes that follow
            child = head
            # we delete this head
            head = None
        else:
            # if we don't find the kth value, increase index and set current heads next node
            # to the next iteration of the traversing. We're saying head.next because
            # it might be the next value that is the kth value, not this current one.
            index+=1
            head.next, child = traverse(head.next,child,k, index)
    # whatever we found for head and child, we just return that
    return head, child
    # TODO
