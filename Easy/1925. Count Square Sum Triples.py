class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        s = set()

        for i in range(n + 1):
            s.add(i * i)
        
        for i in range(1, n):
            for j in range(i + 1, n):
                if (i * i) + (j * j) in s:
                    ans += 1

        return ans * 2
