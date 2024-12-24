class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num <= 9:
            return True

        return num % 10 != 0
        
