class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bin = []

        while n > 0:
            bin += [ n % 2 ]
            n //= 2
        
        print(bin)

        even = 0
        odd = 0

        for i in range(len(bin)):
            if bin[i] == 1:
                if i % 2 != 0:
                    even += 1
                else:
                    odd += 1
        
        return [odd, even]
