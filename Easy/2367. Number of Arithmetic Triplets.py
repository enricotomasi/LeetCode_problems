class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set()

        for it in nums:
            s.add(it)

        ans = 0

        for it in nums:
            if (diff + it) in s and ((diff * 2) + it) in s:
                ans += 1

        return ans
        