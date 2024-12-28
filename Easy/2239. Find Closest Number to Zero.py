class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        abmi = 100001
        ans = -1

        for it in nums:
            if abs(it) < abmi:
                abmi = abs(it)
                ans = it
            elif abs(it) == abmi and ans < it:
                ans = it
        
        return ans