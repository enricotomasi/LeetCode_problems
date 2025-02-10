\class Solution:
    def clearDigits(self, s: str) -> str:
        ans = ""

        for c in s:
            if c.isdigit():
                if len(ans) >= 1:
                    ans = ans[ : len(ans) - 1]
            else:
                ans += c
            
            # print(ans)
        
        return ans     