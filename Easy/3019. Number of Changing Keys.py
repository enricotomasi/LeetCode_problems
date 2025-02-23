class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        st = s.lower()

        ans = 0

        for i in range (1, n):
            if st[i - 1] != st[i]:
                ans += 1
        
        return ans

        