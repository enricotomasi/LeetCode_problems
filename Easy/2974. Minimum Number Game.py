class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(1, n, 2):
            ans += [nums[i]]
            ans += [nums[i - 1]]

        return ans 

        