class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0

        for i in range(n):
            temp = 0
            j = n - 1
            
            while colors[i] == colors[j] and j > i:
                j -= 1
            
            diff = j - i
            ans = max(ans, diff)

        return ans
