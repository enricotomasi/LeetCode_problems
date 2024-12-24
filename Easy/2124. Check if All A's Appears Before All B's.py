class Solution:
    def checkString(self, s: str) -> bool:
        b = False

        for c in s:
            if c == 'a' and b:
                return False
            
            if not b and c == 'b':
                b = True
        
        return True
        
