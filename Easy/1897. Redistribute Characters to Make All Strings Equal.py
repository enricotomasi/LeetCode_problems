class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        d = { }

        for it in words:
            for it2 in it:
                if it2 in d:
                    d[it2] += 1
                else:
                    d[it2] = 1
        
        for it in d:
            if d[it] % len(words) != 0:
                return False
        
        return True