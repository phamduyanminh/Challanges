# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node, it cannot have a cycle
        if not head or not head.next:
            return False
        
        # slowPointer will move one node at a time
        # fastPointer will move two nodes at a time
        slowPointer = head
        fastPointer = head.next

        # Traversing until fastPointer reaches the end of the list
        while fastPointer and fastPointer.next:
            # If both pointers meet, there is a cycle in the linked list
            if slowPointer == fastPointer:
                return True

            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        # If fastPointer reaches the end of the list, no cycle exists
        return False
        