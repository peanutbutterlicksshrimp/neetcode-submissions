class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        s = len(nums)
        for i in range(0,s):
            nums.append(nums[i])
        
        return nums
