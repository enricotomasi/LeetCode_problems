def int2string(n):
    l = []
    
    while n > 0:
        l.append(str(n % 10))
        n //= 10
    
    l.sort()

    return "".join(l)

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        potwo = set()

        for i in range(31):
            p = pow(2, i)
            toadd = int2string(p)
            potwo.add(toadd)
            # print(i, p, toadd)
    
        s = int2string(n)

        return s in potwo