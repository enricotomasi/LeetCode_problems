def sig(word):
    n = len(word)
    ans = ""

    for i in range(1, n):
        diff = ord(word[i]) - ord(word[i - 1])
        ans += str(diff)
        ans += '*'
    
    return ans


class Solution:
    def oddString(self, words: List[str]) -> str:
        m = { }

        for word in words:
            s = sig(word)

            if s in m:
                m[s] += 1
            else:
                m[s] = 1
        
        si = ""

        for it in m:
            if m[it] == 1:
                si = it
        
        for word in words:
            if sig(word) == si:
                return word
        
        return "-1"
