class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        nums = sorted(nums)
        print(nums)
        def dfs(i, s):
            if s > target or i >=len(nums):
                return False
            if s == target:
                res.append(sub.copy())
                return True
            sub.append(nums[i])
            dfs(i, s + nums[i])
            if sub:
                sub.pop()
            if not dfs(i+1,s):
                return False
        dfs(0,0)
        return res