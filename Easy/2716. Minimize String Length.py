class Solution:
    def minimizedStringLength(self, s: str) -> int:
        m = [0 for _ in range(26)]

        for c in s:
            m[ord(c) - ord('a')] += 1

        ans = 0

        for i in range(26):
            if m[i] >= 1:
                ans +=1
        
        return ans
        