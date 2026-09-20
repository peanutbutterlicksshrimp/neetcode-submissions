class Solution:
    def climbStairs(self, n: int) -> int:
        dfs = [0] * (n+1)
        if n <= 2:
            return n
        dfs[1] = 1
        dfs[2] = 2

        for i in range(3, n+1):
            dfs[i] = dfs[i-1] + dfs[i-2]
        
        return dfs[n]