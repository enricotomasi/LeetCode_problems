class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            if s[i] == ' ':
                k -= 1 
                if k == 0:
                    break
            ans += s[i]

        return ans
        
