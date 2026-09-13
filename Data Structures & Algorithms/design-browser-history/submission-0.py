class ListNode:
    def __init__(self, url):
        self.val = url
        self.next = None
        self.prev = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.size = 1
        self.curr = self.head

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.curr
        self.curr.next = node
        self.curr = node

    def back(self, steps: int) -> str:
        c = 0
        while c < steps and self.curr.prev:
            self.curr = self.curr.prev
            c+=1
        
        return self.curr.val

    def forward(self, steps: int) -> str:
        c = 0
        while c < steps and self.curr.next:
            self.curr = self.curr.next
            c+=1
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)