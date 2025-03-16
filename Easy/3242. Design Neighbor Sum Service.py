class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.gr = grid
        self.m = len(grid)
        self.n = len(grid[0])
    
    def findpos(self, n):
        for i in range(self.m):
            for j in range(self.n):
                if self.gr[i][j] == n:
                    return [i, j]
        return [-1][-1] 
        

    def adjacentSum(self, value: int) -> int:
        pos = self.findpos(value)
        # print(f"\nadjacentSum value: {value} pos: {pos}")
        x = pos[0]
        y = pos[1]

        ans = 0

        if x - 1 >= 0:
            ans += self.gr[x - 1][y]
        
        if x + 1 < self.m:
            ans += self.gr[x + 1][y]
        
        if y - 1 >= 0:
            ans += self.gr[x][y - 1]
        
        if y + 1 < self.n:
            ans += self.gr[x][y + 1]

        return ans
        

    def diagonalSum(self, value: int) -> int:
        pos = self.findpos(value)
        # print(f"\ndiagonalSum value: {value} pos: {pos}")
        x = pos[0]
        y = pos[1]

        ans = 0
        
        if x - 1 >= 0 and y -1 >= 0:
            ans += self.gr[x - 1][y - 1]
        
        if x + 1 < self.m and y + 1 < self.n:
            ans += self.gr[x + 1][y + 1]
        
        if x + 1 < self.m and y - 1 >= 0:
            ans += self.gr[x + 1][y - 1]
        
        if x - 1 >= 0 and y + 1 < self.n:
            ans += self.gr[x - 1][y + 1]

        return ans

        


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)