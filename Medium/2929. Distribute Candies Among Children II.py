class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        l = min(limit, n)

        for i in range(l + 1):
            if n - i > limit + limit:
                continue

            ans += min(limit, n - i) - max(n - i - limit, 0) + 1

        return ans
        