class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        double = -1

        m = [0 for _ in range(n * n)]

        for row in grid:
            for val in row:
                m[val - 1] += 1
                if m[val - 1] >= 2:
                    double = val
        
        missing = -1
        for i in range(n * n):
            if m[i] == 0:
                missing = i + 1
                break
        
        return [double, missing]
      
