class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)*2
        size = len(nums)*2
        ogS = len(nums)
        for i in range(0,size):
            if i >= ogS:
                arr[i] = nums[i-ogS]
            else:
                arr[i] = nums[i]
        
        return arr
