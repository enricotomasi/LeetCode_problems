class Solution:
    def findLatestTime(self, s: str) -> str:
        d1 = -1
        d2 = -1
        d3 = -1
        d4 = -1

        if s[0] != '?':
            d1 = ord(s[0]) - ord('0')

        if s[1] != '?':
            d2 = ord(s[1]) - ord('0')

        if s[3] != '?':
            d3 = ord(s[3]) - ord('0')

        if s[4] != '?':
            d4 = ord(s[4]) - ord('0')

        #print(f"{d1}{d2}:{d3}{d4}")

        ans = ""

        if d1 < 0:
            if d2 < 2:
                ans += '1'
            else:
                ans += '0'
        else:
            ans += str(d1)

        if d2 < 0:
            if ans[0] == '1':
                ans += '1'
            else:
                ans += '9'
        else:
            ans += str(d2)
        
        ans += ':'

        if d3 < 0:
            ans += '5'
        else:
            ans += str(d3)

        if d4 < 0:
            ans += '9'
        else:
            ans += str(d4)

        
        return ans