def dec2bin(n):
    ans = ""

    while n > 0:
        ans = str(n % 2) + ans
        n //= 2
    
    return ans

def addzeroes(n, k):
    for i in range(k):
        n = '0' + n
    return n

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        b1 = dec2bin(n)
        b2 = dec2bin(k)

        if len(b1) > len(b2):
            b2 = addzeroes(b2, len(b1) - len(b2))
        elif len(b1) < len(b2):
            b1 = addzeroes(b1, (len(b2) - len(b1)))

        # print(b1)
        # print(b2)

        ans = 0

        for i in range(len(b1)):
            # print(f"{i}# b1: {b1[i]} b2: {b2[i]}")
            if b1[i] != b2[i]:
                if b1[i] == '1':
                    ans += 1
                else:
                    return -1
        
        return ans
      