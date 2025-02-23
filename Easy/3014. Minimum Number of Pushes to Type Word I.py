class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0

        for i in range(n):
            if i < 8:
                ans += 1
            elif i < 16:
                ans += 2
            elif i < 24:
                ans += 3
            else:
                ans += 4
        
        return ans