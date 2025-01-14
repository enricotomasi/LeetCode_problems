class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        ans = []

        for it in nums:
            if it != 0:
                ans += [it]

        for i in range(n - len(ans)):
            ans += [0]
        
        return ans
        
