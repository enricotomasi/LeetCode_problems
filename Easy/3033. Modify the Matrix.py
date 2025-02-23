class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        mc = [0 for _ in range(n)]

        for j in range(n):
            temp = -1
            
            for i in range(m):
                temp = max(temp, matrix[i][j])
            
            mc[j] = temp
        
        ans = []

        for i in range(m):
            temp = []
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = mc[j]
                
        return matrix
                