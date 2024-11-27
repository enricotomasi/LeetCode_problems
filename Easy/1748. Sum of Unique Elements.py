class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = dict()

        for it in nums:
            if it in d:
                d[it] += 1
            else:
                d[it] = 1
        
        ans = 0
        
        for it in d:
            if d[it] == 1:
                ans += it
        
        return ans
        
