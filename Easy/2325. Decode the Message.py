class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dec = { }
        idx = 0

        for c in key:
            if c == ' ' or c in dec:
                continue
            
            dec[c] = chr(idx + ord('a'))
            idx += 1
        
        # print(dec)

        ans = ""

        for c in message:
            if c in dec:
                ans += dec[c]
            else:
                ans += c

        return ans
        
        