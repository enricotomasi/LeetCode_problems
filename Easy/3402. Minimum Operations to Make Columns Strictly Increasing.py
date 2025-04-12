class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        ans = 0

        for i in range(n):
            last = grid[0][i]
            # print(f"\n{i}# {last}")

            for j in range(1, m):
                # print(f"    -> {j}# grid[{j}][{i}]: {grid[j][i]} last: {last}")
                add = 0
                if grid[j][i] < last + 1:
                    add += last - grid[j][i] + 1
                    # print(f"        ----> add {add}")
                
                ans += add
                last = grid[j][i] + add
            
        return ans