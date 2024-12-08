class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        return (nums[n - 2] * nums[n - 1]) - (nums[0] * nums[1]) 