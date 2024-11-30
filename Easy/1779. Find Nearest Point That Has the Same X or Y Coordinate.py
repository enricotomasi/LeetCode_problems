import sys

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        n = len(points)
        ans = -1
        mdist = sys.maxsize

        for i in range(n):
            it = points[i]
            # print(f"\n{i}#  {x}, {y}  *** {it[0]}, {it[1]}  ---  mdist: {mdist}  ans: {ans}")
            if it[0] == x and it[1] == y:
                return i
            if it[0] == x:
                dist = abs(y - it[1])
                # print(f"it[0] == x dist: {dist}")
                
                if dist < mdist:
                    # print("dist < mdist")        
                    mdist = dist
                    ans = i
            elif it[1] == y:
                # print(f"it[1] == y dist: {dist}")
                dist = abs(x - it[0])
                
                if dist < mdist:
                    # print("dist < mdist")
                    mdist = dist
                    ans = i
                 
            # print(f"{i}#  {x}, {y}  *** {it[0]}, {it[1]}  ---  mdist: {mdist}  ans: {ans}")
            
        
        return ans
