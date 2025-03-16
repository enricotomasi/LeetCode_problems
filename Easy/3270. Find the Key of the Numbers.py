def digify(n):
    arr = [0 for _ in range(4)]
    
    pos = 3
    while (n):
        arr[pos] = n % 10
        n //= 10
        pos -= 1
    
    return arr

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        d1 = digify(num1)
        d2 = digify(num2)
        d3 = digify(num3)

        # print(d1, d2, d3)

        arr = [0 for _ in range(4)]

        for i in range(4):
            arr[i] = min(d1[i], d2[i], d3[i])

        ans = 0
        
        for i in range(4):
            ans += arr[i] * pow(10, (3 - i))
        
        return ans