class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        temp = nums[0]

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                temp += nums[i]
            else:
                ans = max(ans, temp)
                temp = nums[i]
        
        return max(ans, temp)



        