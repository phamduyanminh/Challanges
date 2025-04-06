# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        def reverse(node: ListNode) -> ListNode:
            current = node
            prev = None

            while current:
                current.next, prev, current = prev, current, current.next
            return prev
        
        # Find middle point of linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            breakPointer = slow
            slow = slow.next
            fast = fast.next.next
        
        # The second half starts at slow.next
        # First half: 1 -> 2 -> 3 -> None
        # Second half: 4 -> 5 -> None
        right = reverse(slow.next)
        slow.next = None  # Disconnect the left half from the right half
        left = head

        # Merge first-haf and second-half
        while right:
            left.next, right.next, left, right = right, left.next, left.next, right.next 


        