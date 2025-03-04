class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [0 for _ in range(26)]
        upper = [0 for _ in range(26)]

        for c in word:
            if c >= 'a' and c <= 'z':
                lower[ord(c) - ord('a')] += 1
            else:
                upper[ord(c) - ord('A')] += 1

        print(lower)
        print(upper)

        ans = 0

        for i in range(26):
            if lower[i] != 0 and upper[i] != 0:
                ans += 1
                
        return ans        
