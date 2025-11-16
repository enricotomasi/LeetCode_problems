def calc(n):
    ans = 0
    
    for i in range(n):
        ans += i + 1

    return ans

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