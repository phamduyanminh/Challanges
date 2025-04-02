# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base cases: empty list, single node, or no rotation needed
        if k == 0 or head == None or head.next == None:
            return head
        
        # Calculate the length of the list
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        
        # Adjust k in case it's larger than the list length
        k = k % length
        if k == 0:
            return head

        # Function to remove the last node
        def remove_last_node(head: ListNode) -> (ListNode, ListNode):
            currentNode = head
            # Traverse until currentNonde.next is the last node
            while currentNode.next.next:
                currentNode = currentNode.next
            # currentNode.next is the last node to be removed
            removedNode = currentNode.next
            currentNode.next = None 

            return head, removedNode
        
        
        # Function to insert recent removed node and add it at the beginning of the list
        def insert_at_the_beginning(head: ListNode, addedNode: ListNode) -> ListNode:
            # Set new node’s next pointer to the current head of the list
            addedNode.next = head
            return addedNode
        
        # Rotate the list one step at a time for k rotations
        for i in range(0, k):
            head, removedNode = remove_last_node(head)
            head = insert_at_the_beginning(head, removedNode)
        
        return head
        