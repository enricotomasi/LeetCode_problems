class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        last = nums[0]

        for i in range(1, n):
            if last >= nums[i]:
                ans += last - nums[i] + 1
                last = nums[i] + (last - nums[i] + 1)
            else:
                last = nums[i]
        
        return ans
        
