class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new = ""
            
            for i in range(len(s) - 1):
                digit = ((ord(s[i]) - ord('0')) + (ord(s[i + 1]) - ord('0'))) % 10
                new += str(digit)

            s = new

        return s[0] == s[1]
         