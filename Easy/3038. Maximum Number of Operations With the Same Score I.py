class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
        ans = 1
        s = nums[0] + nums[1]
        
        for i in range(3, len(nums), 2):
            if nums[i - 1] + nums[i] == s:
                ans += 1
            else:
                break

        return ans        