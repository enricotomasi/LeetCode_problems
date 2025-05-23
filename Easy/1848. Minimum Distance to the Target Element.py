import sys

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        ans = sys.maxsize

        for i in range(n):
            if nums[i] == target:
                ans = min(ans, abs(i - start))
        
        return ans
