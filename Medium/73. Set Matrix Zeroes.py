class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        blank = 10*50 * - 1

        # print(f"m: {m} n: {n}\n")

        for i in range(m):
            for j in range(n):
                # print(f"{i}, {j}: {matrix[i][j]}", end = " ")
                if matrix[i][j] == 0:
                    # print(" <------> bingo", end = " ")
                    matrix[i][j] = -1
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = blank
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = blank
                    # print(matrix, end = " ")
                # print()
                    
        # print(matrix)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == blank:
                    matrix[i][j] = 0
        