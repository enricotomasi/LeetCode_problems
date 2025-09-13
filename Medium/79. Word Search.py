class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        
        nw = len(word)
        
        n = len(board)
        m = len(board[0])

        def rec(pos, x, y):
            if pos == nw:
                return True

            if x < 0 or y < 0 or x >= n or y >= m or (x, y) in vis or board[x][y] != word[pos]:
                return False

            vis.add((x, y))

            dirx = [1, 0, -1, 0]
            diry = [0, 1, 0, -1]            
            
            ans = False
            
            for i in range(4):
                ans = ans or rec(pos + 1, x + dirx[i], y + diry[i])
            
            vis.remove((x, y))

            return ans

        for i in range(n):
            for j in range(m):
                if rec(0, i, j):
                    return True
        
        return False
        