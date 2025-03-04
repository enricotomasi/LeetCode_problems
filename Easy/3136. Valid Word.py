class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        
        if n < 3:
            return False
        
        vov = False
        cons = False

        for c in word:
            if not c.isdigit() and not c.isalpha():
                return False
            
            if not c.isdigit():
                if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
                    vov = True
                else:
                    cons = True
        
        return vov and cons
