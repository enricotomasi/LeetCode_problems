class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0

        for it in sentences:
            sp = it.split(" ")
            ans = max(ans, len(sp))
            
        return ans
        
