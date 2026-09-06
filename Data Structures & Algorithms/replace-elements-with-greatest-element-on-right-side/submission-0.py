class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        re = []

        for i in range(0,len(arr)-1):
            val = max(arr[i+1:])
            re.append(val)
        re.append(-1)
        return re