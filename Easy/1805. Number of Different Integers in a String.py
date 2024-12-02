class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        temp = ""

        for c in word:
            if c.isdigit():
                temp += c
            else:
                if temp != "":
                    s.add(int(temp))
                    temp = ""
        
        if temp != "":
            s.add(int(temp))
        
        # print(s)

        return len(s)
            

        
