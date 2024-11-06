class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        first = 0
        second = 0
        for i in range(n):
            first += mat[i][i]
            second += mat[i][n - i - 1]
        
        ans = first + second
        
        if n % 2 != 0:
            ans -= mat[n // 2][n // 2]

        return ans
