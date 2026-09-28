class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3

        for i in range(len(nums)):
            count[nums[i]] +=1
        
        i = 0
        for val in range(0,len(count)):
            for j in range(count[val]):
                nums[i] = val
                i+=1
        return nums
        