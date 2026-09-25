# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode(None)
        curr = head
        prev = head
        s = None
        for node in range(len(lists)):
            h2 = lists[node]
            prev = head
            while h2:
                if prev.next and prev.next.val != None and prev.next.val > h2.val:
                    #we need to assign h2 as the next val to prev
                    print("prev.next is larger than h2: ", prev.next.val ," > ", h2.val)
                    nextH2 = h2.next
                    nextPrev = prev.next
                    prev.next = h2
                    h2.next = nextPrev
                    h2 = nextH2
                elif curr.val != None and curr.val > h2.val:
                    # print("curr is larger than h2: ", curr.val ," > ", h2.val)

                    #this handles the case if h2 is larger than our smallest
                    search = prev.next
                    while search.next and search.next.val <= h2.val:
                        search = search.next
                    nextNodeSearch = search.next
                    nextNodeH2 = h2.next
                    search.next = h2
                    h2.next = nextNodeSearch
                    h2 = nextNodeH2
                else:
                    curr.next = h2
                    curr = h2
                    h2 = h2.next
        return head.next