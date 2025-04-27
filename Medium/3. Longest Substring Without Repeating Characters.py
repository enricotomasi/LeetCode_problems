class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        ans = 1
        for i in range(n):
            freq = [0 for _ in range(256)]           
            for j in range(i, n):
                if freq[ord(s[j])] == 1:
                    ans = max(ans, j - i)
                    break
                elif j == n - 1:
                    ans = max(ans, j - i + 1)
                else:
                    freq[ord(s[j])] = 1
                
        return ans