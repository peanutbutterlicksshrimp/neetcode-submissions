class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, k, h):
            n = len(piles)
            time = 0
            for i in range(n):
                time += math.ceil(piles[i]/k)
                #print("time:", time, "piles : ", piles[i])
            
            if time == h:
                return 0
            if time < h:
                return 1 #k too large
            if time > h:
                return -1 #k is too small


        k = max(piles)
        n = len(piles)
        l = 1
        r = k
        prevHigh = k
        while l <= r:
            m = (l+r)//2
            v = check(piles,m, h)
            if v == 0:
                prevHigh = m
                r = m-1
            elif v == 1:
                prevHigh = m
                r = m - 1
            else:
                l = m + 1
        return prevHigh
        






        

    