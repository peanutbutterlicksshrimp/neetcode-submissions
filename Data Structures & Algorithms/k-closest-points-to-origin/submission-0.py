import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map = dict()
        
        x2 = 0
        y2 = 0
        arr = []
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            calc = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            print("this is hte point: ", points[i], " clc; ", calc)
            map[(x1,y1)] = calc

        print(map)
        s = sorted(map.items(), key = lambda item:item[1])
        count = 0
        i = 0
        while count < k and i < len(s):
            print(s[i])
            point,val = s[i]
            i+=1
            count+=1
            arr.append([point[0],point[1]])
        return arr


