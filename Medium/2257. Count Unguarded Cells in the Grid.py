class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['*'] * n for _ in range(m)]
        
        move = [ (-1, 0), (1, 0), (0, 1), (0, -1) ]

        for x, y in walls:
            grid[x][y] = 'W'

        for x, y in guards:
            grid[x][y] = 'G'

        for it in guards:
            for dx, dy in move:
                x = it[0]
                y = it[1]
                while True:
                    x += dx
                    y += dy

                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 'G' or grid[x][y] == 'W':
                        break

                    grid[x][y] = 'g'

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    ans +=1

        return ans