class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = [ ]

        for it in nums:
            temp = []

            while it > 0:
                temp += [ it % 10 ]
                it //= 10

            ans += temp[ : : -1 ]
        
        return ans
        