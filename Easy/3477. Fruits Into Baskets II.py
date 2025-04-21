class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        ans = 0
        
        for it in fruits:
            placed = False
            for i in range(n):
                if baskets[i] >= it:
                    placed = True
                    baskets[i] = 0
                    break
            
            if not placed:
                ans += 1
        
        return ans