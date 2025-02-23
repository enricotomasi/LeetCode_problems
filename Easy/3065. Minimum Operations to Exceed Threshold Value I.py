class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] >= k:
                return i
        
        return -1      