def dec2bin(n):
    ans = ""

    while n > 0:
        ans = str(n % 2) + ans
        n //= 2
    
    return ans


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y = int(date[ : 4 ])
        m = int(date[ 5 : 7 ])
        d = int(date[ 8 : 10 ])

        # print(y, m, d)

        return dec2bin(y) + "-" + dec2bin(m) + "-" + dec2bin(d)