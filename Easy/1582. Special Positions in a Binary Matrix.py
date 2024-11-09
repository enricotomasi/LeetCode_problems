class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        cols = []
        for i in range(n):
            count = 0    
            for j in range(m):
                if mat[j][i] == 1:
                    count += 1
            if count == 1:
                cols += [i]
        
        rows = []
        for i in range(m):
            count = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count += 1
            if count == 1:
                rows += [i]

        
        # print("rows", rows)
        # print("cols", cols)

        ans = 0

        for i in range(m):
            for j in range (n):
                if mat[i][j] == 1 and i in rows and j in cols:
                    ans += 1

        return ans