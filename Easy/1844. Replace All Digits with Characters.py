class Solution:
    def replaceDigits(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(1, n, 2):
            ans += s[i - 1]
            c = ord(s[i - 1]) + ord(s[i]) - ord('0')           
            ans += chr(c)

        if not s[n - 1].isdigit():
            ans += s[n - 1]

        return ans 


        
