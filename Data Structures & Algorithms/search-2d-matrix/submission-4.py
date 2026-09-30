class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        l = 0 
        r = len(matrix) -1
        n = len(matrix[0])
        found = False
        mR = None
        while l <= r:
            mR = (l+r) // 2
            print(mR)
            s = matrix[mR][0]
            end = matrix[mR][n-1]
            if s <= target and end >= target:
                print("found")
                found = True
                break;
            elif target < s:
                r = mR-1
            elif target > end:
                l = mR+1
        
        print("this is found: ", found)
        if not found:
            print("not here")
            return False
        
        j = 0 #l
        k = len(matrix[mR])-1
        while j <= k:
            mN = (j+k) // 2
            if matrix[mR][mN] == target:
                return True
            elif target < matrix[mR][mN]:
                k = mN - 1
            elif target > matrix[mR][mN]:
                j = mN +1
        return False


        

