class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(32):
            c = 0
            p = pow(2, i) 
            
            for it in nums:
                if it & p:
                    c += 1
            if c >= k:
                ans += p
        
        return ans