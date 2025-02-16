class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)

        ans = -1
        maxones = -1

        for i in range(n):
            ones = 0
            
            for j in range(n):
                if grid[i][j] == 1:
                    ones += 1
            
            if ones > maxones:
                maxones = ones
                ans = i
        
        return ans
        