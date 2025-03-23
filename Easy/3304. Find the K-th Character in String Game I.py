class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"

        while (len(s) < k):
            temp = ""
            for c in s:
                if c == 'z':
                    temp += 'a'
                else:
                    temp += chr(ord(c) + 1)
            s += temp
            print(s)
        
        return s[k - 1]