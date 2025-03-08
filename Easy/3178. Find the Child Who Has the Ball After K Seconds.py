class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if k < n:
            return k
        
        n -= 1
        
        if (k // n) % 2 != 0:
            return n - (k % n)

        return k % n