class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()

        start = n * 5 // 100
        end = n - start

        new = arr[start : end]

        return sum(new) / len(new)
