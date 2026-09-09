# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        curr = head.next
        head.next = None
    
        while curr:
            newNode = curr.next
            curr.next = head
            head = curr
            curr = newNode
        return head

