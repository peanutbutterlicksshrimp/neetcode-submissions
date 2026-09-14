class MyStack:

    def __init__(self):
        self.q = deque()
        self.size = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size +=1

        
    def pop(self) -> int:
        print(self.q)
        if self.q:
            self.size-=1
            return self.q.pop()


    def top(self) -> int:
        if self.q:
            return self.q[-1]

    def empty(self) -> bool:
        if self.size > 0:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()