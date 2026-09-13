class ListNode:
    def __init__(self, url):
        self.val = url
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.currIndex = 0
        
    def visit(self, url: str) -> None:
        self.arr = self.arr[:self.currIndex+1]
        self.arr.append(url)
        self.currIndex = len(self.arr)-1

        print("this is hte array now: ", self.arr, "this is hte curr index: ", self.currIndex)
        
    def back(self, steps: int) -> str:
        print("steps Back: ", steps)
        print("self.curr idx: ", self.currIndex)
        print("expected index: ", self.currIndex - steps)

        if self.currIndex - steps < 0:
            self.currIndex = 0
            print("expected val: ", self.arr[self.currIndex])
            return self.arr[0]
        else:
            print("expected val: ", self.arr[self.currIndex - steps])
            self.currIndex-=steps
            val = self.arr[self.currIndex]
        return val

    def forward(self, steps: int) -> str:
        print("steps forward: ", steps)
        print("self.curr idx: ", self.currIndex)
        print("expected index: ", self.currIndex + steps)

        if (self.currIndex + steps) >= len(self.arr):
            self.currIndex = len(self.arr) -1
            print("expected val: ", self.arr[self.currIndex])
            return self.arr[self.currIndex]
        else:
            self.currIndex += steps
            print("expected val: ", self.arr[self.currIndex])
            return self.arr[self.currIndex]



#DLL -------------------------------------
    # def __init__(self, homepage: str):
    #     self.head = ListNode(homepage)
    #     self.size = 1
    #     self.curr = self.head

    # def visit(self, url: str) -> None:
    #     node = ListNode(url)
    #     node.prev = self.curr
    #     self.curr.next = node
    #     self.curr = node

    # def back(self, steps: int) -> str:
    #     c = 0
    #     while c < steps and self.curr.prev:
    #         self.curr = self.curr.prev
    #         c+=1
        
    #     return self.curr.val

    # def forward(self, steps: int) -> str:
    #     c = 0
    #     while c < steps and self.curr.next:
    #         self.curr = self.curr.next
    #         c+=1
    #     return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)