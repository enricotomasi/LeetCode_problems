class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        last = s[0]
        c = 1

        for i in range(1, n):
            if s[i] == last:
                c += 1
            else:
                if c == k:
                    return True
                c = 1
            
            last = s[i]
        
        if c == k:
            return True
        
        return False
                
        