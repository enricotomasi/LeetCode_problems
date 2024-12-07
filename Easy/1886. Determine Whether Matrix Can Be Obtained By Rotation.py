class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m = len(mat)
        n = len(mat[0])

        ok1 = True
        ok2 = True
        ok4 = True
        ok6 = True
        ok7 = True
        ok8 = True
        ok9 = True
        ok10 = True

        for i in range(m):
            for j in range(n):
                if ok1 and mat[i][j] != target[i][j]:
                    ok1 = False
                if ok2 and mat[i][j] != target[m - i - 1][j]:
                    ok2 = False
                if ok4 and mat[i][j] != target[m - i - 1][j]:
                    ok4 = False
                if ok6 and mat[i][j] != target[n - j - 1][i]:
                    ok6 = False
                if ok7 and mat[i][j] != target[m - i - 1][n - j - 1]:
                    ok7 = False
                if ok8 and mat[i][j] != target[n - j - 1][m - i - 1]:
                    ok8 = False
                if ok9 and mat[i][j] != target[m - i - 1][j]:
                    ok9 = False
                if ok10 and mat[i][j] != target[j][m - i - 1]:
                    ok10 = False
                 
        # print(ok1, ok2, ok4, ok6, ok7, ok8, ok9, ok10)
        return ok1 or ok2 or ok4 or ok6 or ok7 or ok8 or ok9 or ok10