class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = 0
        r = sum(nums)

        ans = 0

        for i in range(n - 1):
            l += nums[i]
            r -= nums[i]

            if (l - r) % 2 == 0:
                ans += 1

        return ans