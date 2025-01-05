class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        h = [ -1, -1, -1,  0, 0, 0,  1, 1, 1 ]
        v = [ -1,  0,  1, -1, 1, 0, -1, 0, 1 ]
 
        ans = []
        for i in range(1, n - 1):
            row = []
            
            for j in range(1, n - 1):
                toadd = -1
                for k in range(9):
                    ph = i + h[k]
                    pv = j + v[k]
                    toadd = max(toadd, grid[ph][pv])
                row += [toadd]

            ans += [row]
        
        return ans
        