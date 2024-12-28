class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            temp = 0
            strtemp = ""
            kk = k

            for it in s:
                digit = ord(it) - ord('0')
                print(digit)
                temp += digit

                kk -= 1
                if kk <= 0:
                    strtemp += str(temp)
                    temp = 0
                    kk = k

            if len(s) % k != 0:
                strtemp += str(temp)
            
            s = strtemp

        return s

        