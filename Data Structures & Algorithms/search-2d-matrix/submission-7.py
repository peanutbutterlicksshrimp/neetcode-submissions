class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in matrix:
            print(r)



        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        h = n-1
        v = 0

        print("h: ", h)
        print("v: ", v)

        while h >= 0 and h < n and v >=0 and v < m:
            if matrix[v][h] == target:
                return True
            elif target < matrix[v][h]:
                h-=1
            elif target > matrix[v][h]:
                v+=1
        return False
