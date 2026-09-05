class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            if nums[r] == val:
                r-=1
                continue
            elif nums[l] == val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                r-=1
            else:
                l+=1

        return r+1
