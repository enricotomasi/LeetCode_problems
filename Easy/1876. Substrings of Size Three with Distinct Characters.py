class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)

        if n < 3:
            return 0
        
        ans = 0

        for i in range(2, n):
            # print(s[i - 2], s[i - 1], s[i])
            if s[i - 2] != s[i - 1] and s[i - 2] != s[i] and s[i - 1] != s[i]:
                ans += 1
        
        return ans
