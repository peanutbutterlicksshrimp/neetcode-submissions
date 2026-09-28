class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            j = i - 1
            while j >= 0 and nums[i] < nums[j]:
                #swap
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
                j-=1
                i-=1
        return nums