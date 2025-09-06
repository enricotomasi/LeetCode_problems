class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m - 1
        row = -1

        while start <= end:
            row = (start + end) // 2
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] > target:
                end = row - 1
            else:
                start = row + 1

        if row > 0 and matrix[row][0] > target:
            row -= 1     

        start = 0
        end = n - 1
        col = -1

        while start <= end:
            col = (start + end) // 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = col - 1
            else:
                start = col + 1
        
        return False