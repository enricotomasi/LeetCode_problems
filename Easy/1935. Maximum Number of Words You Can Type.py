class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bl = set()

        for c in brokenLetters:
            bl.add(c)
        
        words = text.split(' ')
        
        ans = 0
        
        for word in words:
            ok = True
            for c in word:
                if c in bl:
                    ok = False
                    break
            
            if ok:
                ans += 1

        return ans
        
