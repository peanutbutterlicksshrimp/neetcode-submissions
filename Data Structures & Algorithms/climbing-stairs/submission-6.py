class Solution:
    def climbStairs(self, n: int) -> int:
        #top down 
        mem = {}
        def dfs(i):
            count = 0
            nonlocal mem
            if i == n:
                return 1
            if i > n:
                return 0
            
            one = i +1
            two = i+2
            if one in mem:
                count+=mem[one]
            else:
                mem[one] = dfs(one)
                count += mem[one]
            if two in mem:
                count+=mem[two]
            else:
                mem[two] = dfs(two)
                count += mem[two]
            return count
        count = dfs(0)

        return count
            