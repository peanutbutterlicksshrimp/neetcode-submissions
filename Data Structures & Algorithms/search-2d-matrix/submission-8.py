class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        C = len(matrix[0])
        s = 0
        e = R*C -1

        while s <= e:
            m = (s+e)//2
            r = m//C
            c = m%C
            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                e = m-1
            else:
                s = m+1
        return False
      