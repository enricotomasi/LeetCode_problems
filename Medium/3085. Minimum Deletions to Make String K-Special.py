import sys 
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        m = dict()

        for c in word:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1

        freqs = []

        for it in m:
            if m[it] != 0:
                freqs.append(m[it])

        ans = sys.maxsize

        for it in freqs:
            temp = 0
            
            for it2 in freqs:
                if (it2 < it):
                    temp += it2
                if (it2 > it + k):
                    temp += it2 - (it + k)
            
            ans = min(ans, temp)

        if ans >= sys.maxsize:
            return 0
        
        return ans

 