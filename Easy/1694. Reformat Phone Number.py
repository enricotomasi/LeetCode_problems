class Solution:
    def reformatNumber(self, number: str) -> str:
        clean = ""

        for c in  number:
            if c.isdigit():
                clean += c
        
        ans = ""
        n = len(clean)
        i = 0

        if (n < 3):
            return clean

        if (n > 4):
            while i < n:
                ans += clean[i]
                i += 1
                if i % 3 == 0 and i != n:
                    ans += "-"
                    if n - i == 4:
                        break

        if i < n - 1:
            ans += clean[i : n - 2]
            ans += "-"
            ans += clean[i + 2 : n]
    
        return ans

        