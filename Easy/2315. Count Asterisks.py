class Solution:
    def countAsterisks(self, s: str) -> int:
        sp = s.split("|")
        
        n = len(sp)
        ans = 0

        for i in range(0, n, 2):
            for c in sp[i]:
                if c == '*':
                    ans += 1
        
        return ans

        