class Solution:
    ans = []

    def rec(self, i, n, arr):
        if i == n:
            self.ans += [arr]

        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            self.rec(i + 1, n, arr[:])
            arr[i], arr[j] = arr[j], arr[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.rec(0, len(nums), nums)
        return self.ans