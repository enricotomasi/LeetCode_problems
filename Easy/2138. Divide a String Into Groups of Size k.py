class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = []

        start = 0

        while start < n:
            ans += [s[start : start + k]]
            start += k
        
        if len(ans[len(ans) - 1]) < k:
            temp = ans[len(ans) - 1]

            for i in range(k - len(temp)):
                temp += fill
            
            ans[len(ans) - 1] = temp
        
        return ans
