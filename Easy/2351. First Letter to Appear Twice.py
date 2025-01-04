class Solution:
    def repeatedCharacter(self, s: str) -> str:
        m = [0 for _ in range(26)]

        for c in s:
            letter = ord(c) - ord('a')
            if m[letter] > 0:
                return c
            else:
                m[letter] = 1
        
        return "-1"