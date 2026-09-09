class MinStack:

    def __init__(self):
        self.stack = []
        self.minS =[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minS) > 0 and self.minS[-1] < val:
            smaller = self.minS.pop()
            self.minS.append(val)
            self.minS.append(smaller)
        else:
            self.minS.append(val)

            

    def pop(self) -> None:
        val = self.stack.pop()
        self.minS.remove(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minS[-1]
