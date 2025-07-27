class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"
        
        n1 = len(num1)
        n2 = len(num2)

        res = []

        c = 0        
        for i in range(n2 - 1, -1, -1):
            d2 = ord(num2[i]) - ord('0')
            
            parz = ""
            for j in range(c):
                parz += '0'
            c += 1
            
            rem = 0
            for j in range(n1 - 1, -1, -1):
                d1 = ord(num1[j]) - ord('0')
                prod = (d2 * d1) + rem
                rem = 0
                if prod > 9:
                    parz = str(prod % 10) + parz
                    rem = prod // 10
                else:
                    parz = str(prod) + parz
            
            if rem > 0:
                parz = str(rem) + parz

            res += [parz]
        
        n = len(res)
        ans = res[n - 1]

        for i in range(n - 2, -1, -1):
            toadd = res[i]
            na = len(ans)
            if na > len(toadd):
                diff = na - len(toadd)
                for j in range(diff):
                    toadd = '0' + toadd
            
            rem = 0
            newans = ""
            for j in range(na - 1, -1, -1):
                a1 = ord(ans[j]) - ord('0')
                a2 = ord(toadd[j]) - ord('0')

                add = a1 + a2 + rem
                rem = 0

                if add > 9:
                    newans = str(add % 10) + newans
                    rem = add // 10
                else:
                    newans = str(add) + newans
            
            if rem > 0:
                newans = str(rem) + newans
                 
            
            ans = newans

        return ans


        