class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        if n <= 0 or s[0] == '0':
            return 0

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one = ord(s[i - 1]) - ord('0')
            two = ((ord(s[i - 2]) - ord('0')) * 10) + (ord(s[i - 1]) - ord('0'))

            # print(one, two)

            if one > 0 and one <= 9:
                dp[i] = dp[i - 1]
            
            if two >= 10 and two <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]
        
        