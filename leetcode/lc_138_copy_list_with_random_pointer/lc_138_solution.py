"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        copyMap = {}

        # First pass: Create a copy of each node and store it in the dictionary
        currentNode = head
        while currentNode:
            copyMap[currentNode] = Node(currentNode.val)
            currentNode = currentNode.next

        # Second pass: Assign next and random pointers
        # Using .get() method helps safely returns None 
        # when currentNode.next or currentNode.random is None
        currentNode = head
        while currentNode:
            copy = copyMap[currentNode]
            copy.next = copyMap.get(currentNode.next) # Returns None if currentNode.next is None
            copy.random = copyMap.get(currentNode.random) # Returns None if currentNode.random is None
            currentNode = currentNode.next
        
        return copyMap[head]


        