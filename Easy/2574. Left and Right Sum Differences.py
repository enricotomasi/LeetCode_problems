class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        tot = 0

        for it in nums:
            tot += it
        
        ans = []

        left = 0

        for it in nums:
            tot -= it
            ans += [abs(tot - left)]
            left += it

        return ans
        