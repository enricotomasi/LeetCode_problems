import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                first = ord(str(nums[i])[0]) - ord('0')
                second = nums[j] % 10
                if math.gcd(first, second) == 1:
                    ans += 1

        return ans                
        