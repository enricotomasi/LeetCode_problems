class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        z = 0
        pos = 0

        for i in range(n):
            if nums[i] == 0:
                z += 1
            
            while z > 1:
                if nums[pos] == 0:
                    z -= 1
                pos += 1
            
            ans = max(ans, i - pos)
        
        return ans
        