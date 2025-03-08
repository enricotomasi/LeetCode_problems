class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        ans = 5000000.5

        nums.sort()

        for i in range(n):
            avg = (nums[i] + nums[n - i - 1]) / 2
            ans = min(ans, avg)
        
        return ans
        