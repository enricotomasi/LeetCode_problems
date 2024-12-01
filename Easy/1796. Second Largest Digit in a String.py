class Solution:
    def secondHighest(self, s: str) -> int:
        m = set()

        for c in s:
            if c.isdigit():
               m.add(ord(c) - ord('0'))
        
        l = list(m)
        l.sort(reverse = True)

        if len(l) < 2:
            return -1
        
        return l[1]

        