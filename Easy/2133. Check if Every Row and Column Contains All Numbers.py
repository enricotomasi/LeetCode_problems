class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for i in range(n):
            check1 = [0 for _ in range(n + 1)]
            check2 = [0 for _ in range(n + 1)]
            
            for j in range(n):
                check1[matrix[i][j]] = 1
                check2[matrix[j][i]] = 1
            
            for j in range(1, n + 1):
                if check1[j] == 0 or check2[j] == 0:
                    return False
        
        return True
        
