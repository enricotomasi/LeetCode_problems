class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        m = [0 for _ in range(26)]
        
        ans = 0
        j = 0
        
        for i in range(n):
            m[ord(s[i]) - ord('a')] += 1
            
            while m[ord(s[i]) - ord('a')] > 2:
                m[ord(s[j]) - ord('a')] -= 1
                j += 1

            ans = max(ans, i - j + 1)
        
        return ans
        