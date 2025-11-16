def calc(n):
    return n * (n + 1) // 2 # Thanx Gauss!

class Solution:
    def numSub(self, s: str) -> int:
        m = pow(10, 9) + 7
        temp = 0
        ans = 0

        for c in s:
            if c == '1':
                temp += 1
            else:
                if temp > 0:
                    ans += calc(temp) % m
                    temp = 0

        if temp > 0:
            ans += calc(temp) % m 

        return ans % m