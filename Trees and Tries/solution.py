# Given an undirected graph, return true if and only if it is bipartite.
# A graph is bipartite if we can split it's set of nodes into two independent
# subsets A and B such that every edge in the graph has one node in A and
# another node in B.
#
# The graph is given in the following form: graph[i] is a list of neighbors for
# node i.  The nodes in the graph are labeled 0,...,len(graph) - 1.
# You are guaranteed V + E <= 1,000,000
# Note that the graph is not necessarily connected.
"""
For this problem, I was trying to make some key observations to understand
what makes a graph bipartite. I did some research on the problem and found that
bipartit graphs are those that are "2-colorable".
Source here: https://www.youtube.com/watch?v=Zg6UAnAzGGs

From this, I could understand a little better on what this question was asking
and found a way to tackle the problem.

The way I went about it was,
We will utilize maps and queues to make search and insertion of items in constant time.

Couple of requirments...
1) First we will have two maps - greenMap and redMap.
2) We will also have a map that keeps track of visited nodes.
3) In addition, we will also have a queue that will keep track of next nodes to visit
4) We will keep track of current node and current color so we can expand to the right
   childs and assign the appropriate color!

Algoritm idea...
1) Set the source node to 0
2) if this node isn't visited yet, add it to visited. If visited, go to the next node in queue
3) if node isn't visited, continue.
4) color this node according to the current color.
5) expand this node
6) for each child, add it to the queue and assign the color OPPOSITE of the currColor,
   which is the parents color. The idea is that childs color should be different than
   parents color.
7) while we're trying to color, if we find that childs color and parents color are the same -
   as in if both parents and child belong in the same color map, then we know graph is not a bipartit.
   For graph to be a bipartite, we need each edges to connect to the nodes from two different node set.
   if they belong in the same color set, then we know a edge connects to two different nodes from
   only ONE set, not BOTH, which makes it non-bipartite. If we find a case like this, we immediately
   return False because we no longer need to continue to check.
8) We break the cycle once the queue's size is zero which means there are no more nodes to visit.
9) Time complexity: O(E + V) because we visit every nodes only once
10) Space Complexity: O(V) because we are storing the nodes in greenMap, redMap, visited, and in Queue.
    overall its linear.
"""
from typing import List
from collections import defaultdict, deque

def is_bipartite(graph: List[List[int]]) -> bool:
    if (graph == None):
        return False

    greenMap = {} # green will be 1
    redMap = {}   # red will be 0
    visited = {}  # visited nodes will fill up as we go through the list
    nextNode = deque() # we will use a queue to keep track of next node

    # initial color is 0 or red and initial node is 0
    currNode = 0
    currColor = 0
    while(True):
        # if currNode is visited, skip this currNode and get the next node from
        # queue and flip the color
        if(currNode in visited):
            currNode = nextNode.popleft()
            if(currColor == 0):
                currColor = 1
            elif(currColor == 1):
                currColor = 0
        else:
            # if not visited, add it to visited list
            visited[currNode] = "V"

        # add current node to approate map based on current color
        if(currColor == 0):
            redMap[currNode] = "R"
        if(currColor == 1):
            greenMap[currNode] = "G"

        # expand this current node
        for i in graph[currNode]:
            # for every child
            if(currNode == 0): # current Node is red, child should NOT appear in redMap
                # if child appears in redMap just return false
                if(i in redMap):
                    return False
                else:
                # else add child to next node to expand and update the appropriate map
                    nextNode.append(i)
                    greenMap[i] = "G"
            if(currNode == 1): # current Node is green, child should NOT appear in greenMap
                if(i in greenMap):
                    return False
                else:
                    nextNode.append(i)
                    redMap[i] = "R"

        # try to get the next node, if fails then break.
        try:
            currNode = nextNode.popleft()
        except:
            break

        # update the color for next node
        if(currColor == 0):
            currColor = 1
        elif(currColor == 1):
            currColor = 0

    return True
