class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0

        for it in nums:
            right += it
                
        for i in range(n):
            right -= nums[i]

            # print(f"{i}#  {left}, {right}")

            if left == right:
                return i
            
            left += nums[i]

        return -1
        