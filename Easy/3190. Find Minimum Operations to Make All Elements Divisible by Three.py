class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0

        for it in nums:
            if it % 3 == 0:
                continue
            
            temp = 5000
            if (it + 2) % 3 == 0 or (it - 2) % 3 == 0:
                temp = 2
            
            if (it + 1) % 3 == 0 or (it - 1) % 3 == 0:
                temp = 1
            
            ans += temp

        return ans
        