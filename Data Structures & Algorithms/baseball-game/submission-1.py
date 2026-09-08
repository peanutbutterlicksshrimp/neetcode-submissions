class Solution:
    total = 0
    def add(self, arr):
        global total
        if len(arr) > 0:
            pop = arr.pop()
            peek = arr[-1]
            arr.append(pop)
            arr.append(pop+peek)
            self.total+= (pop+peek)
    def double(self, arr):
        global total

        if len(arr) > 0:
            val = arr[-1] * 2
            arr.append(val)
            self.total+=val
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        global total
        for i in range(0, len(operations)):
            op = operations[i]
            
            if op == "+":
                self.add(arr)
            elif op == "D":
                self.double(arr)
            elif op == "C":
                if len(arr) > 0:
                    remove = arr.pop()
                    self.total -= remove
            else: #integer
                num = int(op)
                arr.append(num)
                self.total += num
        return self.total


        