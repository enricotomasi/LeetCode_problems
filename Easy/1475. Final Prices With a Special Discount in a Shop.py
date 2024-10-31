class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = []

        for i in range(n - 1):
            # print(f"{i}# prices[i]: {prices[i]}")

            disc = 0
            for j in range(i + 1, n):
                
                if prices[j] <= prices[i]:
                    disc = prices[j]
                    break

                # print(f"   ---> {j}# disc: {disc}  ans: {prices[i] - disc}")
                
            ans += [prices[i] - disc]    

        
        ans += [prices[n - 1]]


        return ans
        
        
