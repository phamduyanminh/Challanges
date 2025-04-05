# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        # Find middle point of linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Traverse from the middle part to the end of linked list
        # and reverse that linked list
        prev = None
        current = slow

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        # Merging first-half and second-half
        # Comment using example 2 for visualization 
        # First-half: [1, 2, 3]
        # Second-half: [5, 4]
        first = head
        second = prev

        while second.next:
            # Save the next pointers
            tempFirst = first.next
            tempSecond = second.next

            # Link first node to second
            first.next = second # 1 -> 5 | 1 -> 5 -> 2 -> 4 | 1 -> 5 -> 2 -> 4 -> 3
            # Link second node to the next node of the first half
            second.next = tempFirst # 1 -> 5 -> 2 | 1 -> 5 -> 2 -> 4 | 1 -> 5 -> 2 -> 4 -> 3 -> None

            # Move to the next nodes in each half
            first = tempFirst
            second = tempSecond
        