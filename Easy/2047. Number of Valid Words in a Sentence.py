class Solution:
    def countValidWords(self, sentence: str) -> int:
        sp = sentence.split()
        ans = 0

        for it in sp:
            n = len(it)
            # print(f"\n{it} len: {n}")
            punc = 0
            dash = 0
            dashpos = -1
            digits = 0
            letters = 0

            for i in range(n):
                c = it[i]
                if c.isnumeric():
                    digits += 1
                    break
                if c == '.':
                    punc += 1
                elif c == '!':
                    punc += 1
                elif c == ',':
                    punc += 1
                elif c == '-':
                    dash += 1
                    dashpos = i
                else:
                    letters +=1
  
            # print(f"punc: {punc} dash: {dash} dashpos: {dashpos} digits: {digits} letters: {letters}")

            if digits > 0 or punc > 1 or dash > 1:
                # print("digits > 0 or punc > 1 or dash > 1")
                continue
        
            if letters == 0 and dash == 1: 
                # print("letters == 0 and dash == 1")
                continue
            
            if dash == 1 and letters < 2:
                # print("dash == 1 and letters < 2")
                continue

            if punc == 1 and it[n - 1].isalpha():
                # print(f"punc == 1 and it[n - 1].isalpha()  it[n - 1]: {it[n - 1]}")
                continue

            if dash == 1 and (dashpos == 0 or dashpos == n - 1):
                # print("dash == 1 and (dashpos == 0 or dashpos == n - 1)")
                continue
            
            # print("ok!")
            ans += 1
                
        return ans
        