# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one node
        if head and not head.next or not head:
            return head

        # Convert linked list to an array of values
        copy = []
        node = head
        while node:
            copy.append(node.val)
            node = node.next
        
        # Traverse the array from right-to-left, 
        # marking elements as 0 if a greater element is found to the right
        current_max = copy[-1]
        for i in range(len(copy)-2, -1, -1):
            if copy[i] < current_max:
                copy[i] = 0
            else:
                current_max = copy[i]

        # Filter out the zeros
        filtered = [x for x in copy if x !=0 ]

        # Reconstruct the linked list using a dummy node
        result = ListNode(0)
        current = result
        for i in filtered:
            current.next = ListNode(i)
            current = current.next

        return result.next


        