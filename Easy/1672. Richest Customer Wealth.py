class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        n = len(accounts[0])

        ans = 0

        for i in range(m):
            tot = 0
            for j in range(n):
                tot += accounts[i][j]
            ans = max(ans, tot)
        
        return ans