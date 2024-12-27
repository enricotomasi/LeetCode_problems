class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        m = { }

        for it in nums:
            if it in m:
                m[it] += 1
            else:
                m[it] = 1
        
        for it in m:
            if m[it] %2 != 0:
                return False
        
        return True
        
