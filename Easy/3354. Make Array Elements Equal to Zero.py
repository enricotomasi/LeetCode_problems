class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        r = 0

        for it in nums:
            r += it

        l = 0
        
        ans = 0
        
        for it in nums:
            if it == 0:
                if r == l:
                    ans += 2
                elif r == l + 1 or r == l - 1:
                    ans += 1
            
            r -= it
            l += it

        return ans
        