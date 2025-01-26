class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = -1

        for it in nums:
            m = max(m, it)

        ans = 0

        for i in range(m, m + k):
            ans += i
        
        return ans
        