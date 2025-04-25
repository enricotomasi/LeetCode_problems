class Solution:
    def maxSum(self, nums: List[int]) -> int:
        used = set()
        ans = 0

        for it in nums:
            if it not in used and it > 0:
                ans += it
                used.add(it)
                
        if ans == 0:
            ans = -500
            for it in nums:
                ans = max(ans, it)
        
        return ans