class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        ans = []

        for it in nums:
            temp += it
            ans += [temp]
        
        return ans
        
