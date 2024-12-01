class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        m1 = { }
        for c in s1:
            if c in m1:
                m1[c] += 1
            else:
                m1[c] = 1
        
        m2 = { }
        for c in s2:
            if c in m2:
                m2[c] += 1
            else:
                m2[c] = 1
        
        
        if len(m1) != len(m2):
            return False
        
        m1 = dict(sorted(m1.items()))
        m2 = dict(sorted(m2.items()))

        if m1 != m2:
            return False
        
        n = len(s1)
        diff = 0

        for i in range(n):
            if s1[i] != s2[i]:
                if diff > 2:
                    return False;
                else:
                    diff += 1

        return diff == 2
        