class Solution:
    
    def add(self, arr):
        if len(arr) > 0:
            pop = arr.pop()
            peek = arr[-1]
            arr.append(pop)
            arr.append(pop+peek)
    def double(self, arr):
        if len(arr) > 0:
            val = arr[-1] * 2
            arr.append(val)
    def calPoints(self, operations: List[str]) -> int:
        arr = []

        for i in range(0, len(operations)):
            op = operations[i]
            
            if op == "+":
                self.add(arr)
            elif op == "D":
                self.double(arr)
            elif op == "C":
                if len(arr) > 0:
                    remove = arr.pop()
            else: #integer
                num = int(op)
                arr.append(num)
        return sum(arr)


        