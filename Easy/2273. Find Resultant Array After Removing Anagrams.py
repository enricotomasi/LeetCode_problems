def cw(s):
    ans = [0 for _ in range(26)]

    for c in s:
        ans[ord(c) - ord('a')] += 1
    
    return ans


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        changes = 69

        while changes > 0 and len(words) > 1:
            new = [words[0]]
            n = len(words)
            m1 = cw(words[0])
            
            # print()
            # print(f"Changes  : {changes}")
            # print(f"words    : {words}")
            # print(f"n        : {n}")
            # print(f"words[0] : ")
            # print(f"m1       : {m1}")

            changes = 0
            

            for i in range(1, n):
                m2 = cw(words[i])
                ana = True
                
                # print()
                # print(f" -> i:         : {i}")
                # print(f" -> words[0]   : {words[0]}")
                # print(f" -> words[{i}]   : {words[i]}")
                # print(f" -> m1         : {m1}")
                # print(f" -> m2         : {m2}")
                
                for j in range(26):
                    if m1[j] != m2[j]:
                        ana = False
                        break
                
                if not ana:
                    new += [words[i]]
                else:
                    changes += 1
                    
                m1 = list(m2)
            
            words = new
        
        return words
