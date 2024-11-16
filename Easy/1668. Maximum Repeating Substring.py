class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ns = len(sequence)
        nw = len(word)

        ans = 0
        rep = 0

        for i in range(ns - nw + 1):
            if (sequence[i] == word[0]):
                if nw == 1:
                    rep += 1
                else:
                    j = 1
                    rep = 0
                    for ii in range(i + 1, ns):
                        if (sequence[ii] != word[j]):
                            break
                        j += 1
                        if (j >= nw):
                            rep += 1
                            j = 0
            else:
                rep = 0
            ans = max(ans, rep)
        
        return ans

        