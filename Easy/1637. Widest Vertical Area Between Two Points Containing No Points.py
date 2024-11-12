class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [ ]

        for it in points:
            x += [ it[0] ]
        
        x.sort()
        #print(x)

        ans = - 1
        n = len(x)

        for i in range(n - 1):
            ans = max(ans, abs(x[i] - x[i + 1]))

        return ans
        
