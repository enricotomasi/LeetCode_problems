class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        
        if n < 8:
            return False
        
        alpha = False
        lower = False
        upper = False
        digit = False
        special = False

        specials = "!@#$%^&*()-+"

        last = "_"

        for i in range(n):
            c = password[i]
            
            if c == last:
                return False
            
            last = c

            if c.isalpha():
                alpha = True
                if c.isupper():
                    upper = True
                else:
                    lower = True
            elif c.isdigit():
                digit = True
            elif c in specials:
                special = True

        
        return alpha and lower and upper and digit and special