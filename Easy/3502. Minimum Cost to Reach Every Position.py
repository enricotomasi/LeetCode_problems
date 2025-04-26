class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        ans = [0 for _ in range(n)]
        ans[0] = cost[0]
        
        for i in range(1, n):
            ans[i] = min(cost[i], ans[i - 1])
        
        return ans