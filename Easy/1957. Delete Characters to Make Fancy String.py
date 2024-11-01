class Solution:
    def makeFancyString(self, s: str) -> str:
        last = '@'
        count = 0
        ans = ""

        for c in s:
            if c == last:
                count += 1
                if count < 3:
                    ans += c
            else:
                ans += c
                count = 1
                last = c
        
        return ans
        