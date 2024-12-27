class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bs = ""
        while start > 0:
            if start % 2 == 1:
                bs += "1"
            else:
                bs += "0"
            start //= 2
        
        bg = ""
        while goal > 0:
            if goal % 2 == 1:
                bg += '1'
            else:
                bg += '0'
            goal //= 2
        
        # print(bs)
        # print(bg)

        ns = len(bs)
        ng = len(bg)

        if ns > ng:
            for i in range(ns - ng):
                bg += '0'
        elif ns < ng:
            for i in range(ng - ns):
                bs += '0'
                
        # print(bs)
        # print(bg)

        ans = 0

        for i in range(len(bs)):
            if bs[i] != bg[i]:
                ans +=1

        return ans
        
