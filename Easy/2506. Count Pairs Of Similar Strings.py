class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        m = { }

        for word in words:
            sig = [0 for _ in range(26)]
            
            for c in word:
                sig[ord(c) - ord('a')] = 1
            
            sigstring = ""

            for it in sig:
                sigstring += str(it)
            
            m[word] = sigstring
         
        ans = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if m[words[i]] == m[words[j]]:
                    ans += 1

        return ans // 2 
