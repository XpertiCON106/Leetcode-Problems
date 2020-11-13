# Given a binary tree, verify it is a binary search tree.
# The tree will be passed as Generator of ints.
# The order will be the level order traversal of a complete
# binary tree with None in place of an integer if that child doesn't exist.
# Think of this as the array representation of a heap.
# For parent i, left child is at 2*i+1 and right child is at 2*i+2
# You are guaranteed the Generator will have no more than 1,000,000 integers
# You are guaranteed all integers will be unique
# You are guaranteed the generator will contain 2^h - 1 elements where
# h is the number of levels in the tree

# You can convert the generator to a list, iterate over it as if it were
# a list, or call the next() method to get the next value (i.e next(tree)).
# We have provided a Node class if you want to parse it into a tree.
# Generators throw a StopIteration exception if next is called and
# the generator has no more values.
# Refer to https://wiki.python.org/moin/Generators for more information.

from typing import Generator
"""
For this problem, I decided to take advantage of what was given.
Which is that the left child of the i'th node is 2*i+1 and right child being
2*i + 2.

This is my overall approach.

1) convert tree generator to list
2) get the parent using index i, which is set to 0 in the beggining
3) if parnets is equal to None, go to the next index
3) get the left child using 2 * i + 1
4) get the right child using 2 * i + 2
5) if the child index goes beyond the list, set the child to None

From here we will do a couple of checks.
More specifically, we will check for whether or not the following condition holds up

left child < parent < right child

if at any point, we break that condition, we return false because it is no longer
a binary search tree. That is what my algorithm basically does

Time complexity: First I turn the generator to a list and then I go through that list once.
                 so my overall time complexity is O(n + n) or O(N)

Space complexity: The only space I create is the list that is converted from the generator.
                  So overall space complexity is O(N)

"""
def is_bst(tree: Generator[int, None, None]) -> bool:
    #left child = 2*i + 1
    #right child = 2*i + 2
    # if tree is empty, implicitly assume its a binary search tree
    if (tree == None):
        return True

    # convert tree to list
    lst = list(tree)

    # first node will be first item in the list
    i = 0
    while(True):
        # try to get the current node and set it to p as in parent
        try:
            p = lst[i]
        except:
            break;

        # if current node is None, go to next node
        if (p == None):
            continue

        # get the left child
        try:
            lc = lst[2*i + 1]
        except:
            lc = None;

        # get the right child
        try:
            rc = lst[2*i + 2]
        except:
            rc = None;

        # if both child is None, go to the next node
        if(lc == None and rc == None):
            i+=1
            continue

        # if parent is less than left child, that violates our condition, so just return false
        if(p < lc and lc != None):
            return False

        # if parent is greater than right child, that violates our condition, so just return false
        if(p > rc and rc != None):
            return False

        # if left child is greater than right child, that also violates our condition, so just return false
        if(lc > rc):
            return False

        # go to the next node
        i+=1


    # if none of those conditions were triggered, we know that this is a BST so we just return true
    return True;
