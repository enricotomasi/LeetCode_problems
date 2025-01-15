class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        tot = (n * (n + 1)) // 2 # Thanx Gauss!
        tot2 = 0

        for i in range(1, n + 1):
            tot2 += i

            # print(f"{i}# {tot}, {tot2}")
            
            if tot == tot2:
                return i
            
            tot -= i

        return -1
        
