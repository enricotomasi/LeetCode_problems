class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        copy = list(nums)
        copy.sort()

        s = []

        for i in range(n - 1, n - k - 1, - 1):
            s += [copy[i]]

        ans = []

        for it in nums:
            if it in s:
                ans += [it]
                s.remove(it)

        return ans
        
