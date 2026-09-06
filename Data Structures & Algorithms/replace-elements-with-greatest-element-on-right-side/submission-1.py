class Solution:
    def findMax(self, l, arr):
        m = arr[l+1];
        for i in range(l+1, len(arr)):
            if arr[i] >= m:
                m = arr[i]
        return m
    
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0, len(arr)-1):
            arr[i] = self.findMax(i, arr)
        arr[-1] = -1
        return arr