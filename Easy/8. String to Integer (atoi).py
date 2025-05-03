class Solution:
    def myAtoi(self, s: str) -> int:
        clean = ""
        neg = False
        start = False

        for c in s:
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                start = True
                if c == '0' and len(clean) == 0:
                    continue
                clean += c
            elif c == '-' and not start:
                start = True
                if len(clean) > 0:
                    break
                else:
                    neg = True
            elif c == ' ':
                if start:
                    break
                else:
                    continue
            elif c == '+':
                if start:
                    break
                else:
                    start = True
                    continue
            else:
                break

        #print(f"*{clean}*") 
        ans = 0
        
        if len(clean) > 0:
            ans = int(clean)
        
        if neg:
            if ans > pow(2, 31):
                return pow(2, 31) * -1
            else:
                ans *= - 1
        elif ans > pow(2, 31) - 1:
            return pow(2, 31) - 1
        
        
        return ans