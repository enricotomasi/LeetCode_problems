class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)

        l = 0

        for i in range(n):
            if s[i] == letter:
                l += 1
                
        return int(l / n * 100)
