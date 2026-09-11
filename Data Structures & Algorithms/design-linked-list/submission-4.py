class MyLinkedList:

    def __init__(self):
        self.arr = []

    def get(self, index: int) -> int:
        if len(self.arr) > index:
            val = self.arr[index]
            return val
        return -1

    def addAtHead(self, val: int) -> None:
        self.arr.insert(0,val)


    def addAtTail(self, val: int) -> None:
        
        self.arr.insert(len(self.arr),val)

    def addAtIndex(self, index: int, val: int) -> None:
        if len(self.arr) == index:
            self.arr.append(val)
        elif len(self.arr) > index:
            self.arr.insert(index,val)
        
    def deleteAtIndex(self, index: int) -> None:
        if len(self.arr) > index:
            self.arr.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)