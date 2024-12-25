class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        # print(f"n: {n}")
        ans = 0

        if n < 3:
            for i in range(n):
                ans += cost[i]
            
            return ans
            
        cost.sort(reverse = True)
        # print(cost)

        for j in range(0, n - 2, 3):
            ans += cost[j] + cost[j + 1]
            # print(f"{j}# {cost[j]} {cost[j + 1]}  ***  ans: {ans}")

        # print(f"\nj: {j}\n  ***  ans: {ans}")
        
        for i in range(n - (n %3), n):
            # print(f"{i}# {cost[i]}  ***  ans: {ans}")
            ans += cost[i]
        
        return ans


        
        