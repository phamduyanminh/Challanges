# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Base case for empty or single-node list
        if not head or not head.next:
            return True
        
        # Store list values in a Python list
        nodeArray = []
        current = head
        while current:
            nodeArray.append(current.val)
            current = current.next
        
        # Check if the list is a palindrome
        # Use two pointers in nodeArray, one at the beginning, one at the end
        left = 0
        right = len(nodeArray)-1
        while left < right:
            if nodeArray[left] != nodeArray[right]:
                return False
            left += 1
            right -= 1

        return True