class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        mid = n // 2    
        va = 0
        vb = 0

        for i in range(n):
            c = s[i].lower()
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                if i < mid:
                    va += 1
                else:
                    vb += 1
        
        return va == vb