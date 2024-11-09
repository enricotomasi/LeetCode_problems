class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        f = 0
        
        for i in range(n):
            f = f - (i + 1) // 2 + (n - i + 1 ) // 2
            ans += f * arr[i]

        return ans