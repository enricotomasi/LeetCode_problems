class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n == 1:
            return s
        
        if n == 2:
            if s[0] != s[1]:
                return s[0]
            else:
                return s

        ans = s[0]

        for i in range(n):
            if len(ans) >= n - i:
                break
            for j in range(n - 1, i, -1):
                if s[i] == s[j]:
                    a = i + 1
                    b = j - 1

                    ok = True
                    while a < b:
                        if s[a] != s[b]:
                            ok = False
                            break
                        a += 1
                        b -= 1
                    
                    if ok and j - i + 1 > len(ans):
                        ans = s[i : j + 1]
                        break

        return ans       