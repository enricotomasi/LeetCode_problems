class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0

        for it in nums:
            if it == 0:
                return 0
            elif it < 0:
                neg += 1
        
        if neg % 2 == 0:
            return 1
        
        return -1
        
