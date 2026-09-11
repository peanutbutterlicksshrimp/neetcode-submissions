# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def smallerL1(self, list1Node, list2Node):
        if list1Node == None:
            return False
        elif list2Node == None:
            return True
        elif list1Node.val < list2Node.val:
            return True
        else:
            return False


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: 
            return list2
        if list2 == None:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)

            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
           

            
            # while arr:
            #     p = arr.pop()
            #     print(p.val)
            #arr should be a list of nodes






            # prev = None
            # curr = None
            # if self.smallerL1(list1, list2):
            #     curr = list1
            #     list1 = list1.next   
            # else:
            #     curr = list2
            #     list2 = list2.next


            # while curr:
            #     curr.next = prev
            #     prev = curr
            #     if self.smallerL1(list1, list2):
            #         curr = list1
            #         if list1:
            #             list1 = list1.next
            #     else:
            #         curr = list2
            #         if list2:
            #             list2 = list2.next
            

            # curr = prev
            # prev = None

            # while curr:
            #     newNode = curr.next
            #     curr.next = prev
            #     prev = curr
            #     curr = newNode
            # return prev
            
            

                

                



