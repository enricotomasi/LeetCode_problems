class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        tots = n * n
        totw = maxWeight // w

        return min (tots, totw)
        