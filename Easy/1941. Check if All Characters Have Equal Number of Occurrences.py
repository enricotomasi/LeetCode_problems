class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = { }

        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        freq = list(d.values())[0]

        for it in d:
            if d[it] != freq:
                return False
        
        return True
