class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0

        for it in nums:
            sum |= it
        
        return sum << (n - 1)
        
