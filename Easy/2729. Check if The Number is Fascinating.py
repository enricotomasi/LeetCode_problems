class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = str(n + n)
        n3 = str(n * 3)

        nt = str(n) + n2 + n3

        check = [0 for _ in range(10)]

        for c in nt:
            check[ord(c) - ord('0')] += 1
        
        # for c in nt:
            # print(c, end = " ")
        # print()
        # print(check)
        
        if check[0] > 0:
            return False
        
        for i in range(1, 10):
            if check[i] != 1:
                return False
        
        return True
