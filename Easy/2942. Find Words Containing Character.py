class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        ans = []

        for i in range(n):
            ok = False
            for c in words[i]:
                if c == x:
                    ok = True
                    break

            if ok:
                ans += [i]
        
        return ans