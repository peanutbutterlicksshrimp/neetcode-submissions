# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        if head == None:
            return None
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        head1 = arr.pop()
        head2 = head1
        while arr:
            node = arr.pop()
            head2.next = node
            head2 = node
        head2.next = None
        return head1