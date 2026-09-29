class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         nums=[-1,0,3,5,9,12]
# m = 5//2 = 2.5 -> 2
# r = m-1 -> 1
# m = 0 + 1 // 2 = 


        def bs(nums,l, r): 
            m = (l+r)//2
            if l > r: 
                return -1
            
            if nums[m] == target:
                return m
            if target > nums[m]:
                print("lower:", l)
                l = m+1
            else:
                r = m-1
            return bs(nums, l, r)
        val = bs(nums, 0, len(nums)-1)

        print("val", val)
        if nums[val] == target:
            return val
        else:
            return -1


        
        