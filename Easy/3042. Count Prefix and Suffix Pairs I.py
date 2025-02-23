def ispre(word1, word2):
    n1 = len(word1)
    n2 = len(word2)

    if n2 < n1:
        return False

    ok = True

    for i in range(n1):
        if word1[i] != word2[i]:
            ok = False
            break
    
    if not ok:
        return False

    j = n2 - 1

    for i in range(n1 - 1, -1, -1):
        if word1[i] != word2[j]:
            ok = False
            break
        j -= 1
    
    return ok

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):
                if ispre(words[i], words[j]):
                    print(words[i], words[j])
                    ans += 1
        
        return ans