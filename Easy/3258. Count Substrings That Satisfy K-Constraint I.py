class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            ones = 0
            zeroes = 0

            for j in range(i, n):
                # print(s[j], end = "")
                if s[j] == '1':
                    ones += 1
                else:
                    zeroes += 1
                
                if ones > k and zeroes > k:
                    break
                
                ans += 1

            # print()

        return ans

        