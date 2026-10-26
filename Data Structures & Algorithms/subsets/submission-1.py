class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in range(0, len(nums)):
            val = nums[i]
            for j in range(0, len(res)):
                s = res[j].copy()
                s.append(val)
                res.append(s)
        return res

                