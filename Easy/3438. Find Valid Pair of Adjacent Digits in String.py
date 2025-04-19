class Solution:
    def findValidPair(self, s: str) -> str:
        m = [0 for _ in range(10)]

        for c in s:
            m[ord(c) - ord('0')] += 1
        
        ans = ""

        vis = [False for _ in range(10)]
        ok = set()

        for i in range(1, 10):
            if m[i] == i:
                ok.add(i)


        for i in range(len(s) - 1):
            d1 = ord(s[i]) - ord('0')
            d2 = ord(s[i + 1]) - ord('0')
        
            if d1 != d2 and d1 in ok and d2 in ok:
                return s[i] + s[i + 1]
                 
        return ""