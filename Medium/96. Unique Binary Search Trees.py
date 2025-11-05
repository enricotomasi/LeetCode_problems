import math
class Solution:
    def numTrees(self, n: int) -> int:
        return int((math.factorial(n * 2)) / (math.factorial(n + 1) * factorial(n)))
