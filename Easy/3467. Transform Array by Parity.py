class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 0

        for it in nums:
            if it % 2 == 0:
                even += 1
            else:
                odd += 1
        
        ans = [0 for _ in range(even)]
        ans += [1 for _ in range(odd)]

        return ans

        