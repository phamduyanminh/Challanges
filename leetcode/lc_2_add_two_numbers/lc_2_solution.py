# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point of the result linked list
        dummyNode = ListNode()
        # 'result' will always point to the dummy node, which helps us return the final list
        result = dummyNode
        
        # 'sum' holds the temporary sum for each digit addition
        # 'carry' holds any carry-over value when the sum of two digits exceeds 9
        sum = 0
        carry = 0

        # Loop through both linked lists until there are no more nodes to process and no carry remains
        while l1 or l2 or carry:
            # Start with the carry from the previous addition
            sum = carry

            # If there is a node in l1, add its value to sum and move to the next node
            if l1:
                sum += l1.val
                l1 = l1.next
            # If there is a node in l2, add its value to sum and move to the next node
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # Create a new node with the digit value (sum modulo 10) and attach it to the result list
            dummyNode.next = ListNode(sum%10)
            # Update the carry (sum divided by 10 gives us the carry for the next iteration)
            carry = sum // 10
            # Move the pointer forward to next node
            dummyNode = dummyNode.next
        
        # Return the head of the new list (skip the dummy node)
        return result.next

        