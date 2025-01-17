class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = 0
        ds = 0

        for it in nums:
            s += it

            while it > 0:
                ds += it % 10
                it //= 10
            
        
        return abs(s - ds)
        
