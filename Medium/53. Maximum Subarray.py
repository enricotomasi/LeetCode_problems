class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        ans = nums[0]

        for n in nums:
            if temp < 0:
                temp = 0

            temp += n
            ans = max(ans, temp)
        
        return ans