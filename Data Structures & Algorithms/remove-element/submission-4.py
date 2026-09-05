class Solution:
    def remove(self, nums, reId):
        for i in range(reId, len(nums)-1):
            nums[i] = nums[i+1]
        return nums;

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        size = len(nums)
        while i < size:
            if nums[i] == val:
                nums = self.remove(nums, i);
                size-=1
            else:
                i+=1

        return size
