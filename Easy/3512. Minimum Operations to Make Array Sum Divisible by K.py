class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = 0

        for it in nums:
            s += it

        ans = 0

        while s % k != 0:
            ans += 1
            s -= 1

        return ans      