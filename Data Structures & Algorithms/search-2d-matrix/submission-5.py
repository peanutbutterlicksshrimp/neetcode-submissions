class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
    
        for m in range(0,len(matrix)):
            for n in range(0,len(matrix[0])):
                if matrix[m][n] == target:
                    return True
        return False
                

        