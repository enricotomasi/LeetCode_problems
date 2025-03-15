class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0

        for it in nums:
            if it < 10:
                single += it
            else:
                double += it
        
        return single != double
        