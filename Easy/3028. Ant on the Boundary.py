class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s = 0
        ans = 0 

        for it in nums:
            s += it
            if s == 0:
                ans += 1
        
        return ans