class Solution:
    def climbStairs(self, n: int) -> int:
        p1 = 0
        p2 = 0
        if n <= 2:
            return n
        p1 = 1 #this is 2 behind
        p2 = 2 #this is 1 behind
        curr = 0
        for i in range(3, n+1):
            curr = p1 + p2
            p1 = p2
            p2 = curr
            
        return curr