import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc(point):
            x2 = point[0]
            y2 = point[1]
            return math.sqrt((0 - x2)**2 + (0 - y2)**2)

        def sort(points, s, e):
            if e-s +1 <= 1:
                return points
            
            piv = calc(points[e])
            left = s
            for i in range(s,e):
                val = calc(points[i])
                if val <= piv:
                    t = points[i]
                    points[i] = points[left]
                    points[left] = t
                    left+=1
            
            t = points[e]
            points[e] = points[left]
            points[left] = t

            sort(points, s, left-1)
            sort(points, left+1, e)
            return points
        sort(points, 0, len(points)-1)
        return points[:k]
        
    
