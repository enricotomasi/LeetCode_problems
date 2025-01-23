def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        rows = len(nums)
        cols = len(nums[0])

        # print(f"rows: {rows} cols: {cols}")

        ans = 0

        for i in range(rows):
            if prime(nums[i][i]):
                ans = max(ans, nums[i][i])

            if prime(nums[i][cols - i - 1]):
                ans = max (ans, nums[i][cols - i - 1])

        return ans