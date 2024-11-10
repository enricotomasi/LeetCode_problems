class Solution:
    def reorderSpaces(self, text: str) -> str:
        temp = ""
        spaces = 0
        arr = []

        for c in text:
            if c == " ":
                spaces += 1
                if temp != "":
                    arr += [temp]
                    temp = ""
            else:
                temp += c


        if (temp != ""):
            arr += [temp]
         
        la = len(arr)
        
        if la == 1:
            ans = arr[0]
            
            for i in range(spaces):
                ans += " "
            
            return ans

        if spaces == 1:
            return text

        sp = spaces // (la - 1)
        rem = spaces % (la - 1)

        ans = ""

        for i in range(la - 1):
            ans += arr[i]
            for j in range(sp):
                ans += " "
        
        ans += arr[la - 1]

        for i in range(rem):
            ans += " "

        return ans


        