class Solution:
    def greatestLetter(self, s: str) -> str:
        lower = [0 for _ in range(26)]
        upper = [0 for _ in range(26)]

        for c in s:
            if c.isupper():
                upper[ord(c) - ord('A')] += 1
            else:
                lower[ord(c) - ord('a')] += 1

        for i in range(25, -1, -1):
            if upper[i] > 0 and lower[i] > 0:
                return chr(i + ord('A'))
        
        return ""
        