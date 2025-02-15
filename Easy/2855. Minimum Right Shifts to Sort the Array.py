class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)

        c = 0
        ans = 0

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                c += 1
                ans = n - i - 1
        
        if c >= 2:
            return - 1
        
        return ans