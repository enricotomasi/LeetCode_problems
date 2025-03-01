class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        n = len(s)
        rev = s[ : : -1 ]

        for i in range(1, n):
            st = s[i - 1] + s[i]
            if st in rev:
                return True
        
        return False