class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        low = 101
        hi = -1

        for it in nums:
            low = min(low, it)
            hi = max(hi, it)
        
        # print(low, hi)
        for it in nums:
            if it != low and it != hi:
                return it

        return -1