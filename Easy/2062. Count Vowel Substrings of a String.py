class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vov = []
        temp = ""
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0

        for c in word:
            if c == 'a':
                a += 1
                temp += c
            elif c == 'e':
                e += 1
                temp += c
            elif c == 'i':
                i += 1
                temp += c
            elif c == 'o':
                o += 1
                temp += c
            elif c == 'u':
                u += 1
                temp += c
            else:
                if temp != "":
                    if a >= 1 and e >= 1 and i >= 1 and o >= 1 and u >= 1:
                        vov += [temp]
                    temp = ""
                    a = 0
                    e = 0
                    i = 0
                    o = 0
                    u = 0
        
        if temp != "" and a >= 1 and e >= 1 and o >= 1 and u >= 1:
            vov += [temp]

        # print(vov)
        ans = 0

        for it in vov:
            n = len(it)
            for q in range(n):
                a = 0
                e = 0
                i = 0
                o = 0
                u = 0
                
                for r in range(q, n):
                    if it[r] == 'a':
                        a += 1
                    elif it[r] == 'e':
                        e += 1
                    elif it[r] == 'i':
                        i += 1
                    elif it[r] == 'o':
                        o += 1
                    elif it[r] == 'u':
                        u += 1
                    
                    if a >= 1 and e >= 1 and i >= 1 and o >= 1 and u >= 1:
                        ans += 1
                    
        return ans
        