class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for it in words:
            if len(it) == 1:
                return it

            start = 0
            end = len(it) - 1
            ok = True

            while start < end:
                if it[start] != it[end]:
                    ok = False
                    break
                start += 1
                end -= 1
                
            if ok:
                return it

        return ""
        
