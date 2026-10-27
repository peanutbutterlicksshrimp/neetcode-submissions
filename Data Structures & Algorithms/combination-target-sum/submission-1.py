class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def bt(i, s):
            
            if i >= len(nums):
               # print("End of arr: ", sub)
                return False
            #print("sum b4: ", s)
            # s+=nums[i]
            if s > target:
              #  print("Larger than target: ", sub, " | ", s)
                return False
            if s == target:
              #  print("Found: ", sub)
                res.append(sub.copy())
                return True
            sub.append(nums[i])
            bt(i,s + nums[i])
            if sub:
                sub.pop()
            bt(i+1,s)
        bt(0,0)
        return res

            
            
            
            