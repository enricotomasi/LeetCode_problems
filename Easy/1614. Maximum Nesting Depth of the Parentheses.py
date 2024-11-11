class Solution:
    def maxDepth(self, s: str) -> int:
        par = 0
        ans = 0

        for c in s:
            if c == "(":
                par += 1
            elif (c == ")"):
                par -=1
            
            ans = max(ans, par)
        
        return ans
            
        
