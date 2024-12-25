class Solution:
    def countElements(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        ans = 0

        for it in nums:
            if it != nums[0] and it != nums[n - 1]:
                ans += 1

        return ans
        