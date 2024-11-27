class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        last = 0
        ans = 0

        for it in gain:
            last += it
            # print(last)
            ans = max(ans, last)
        
        return ans
        
