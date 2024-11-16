class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ""
        for it in word1:
            s1 += it
        
        s2 = ""
        for it in word2:
            s2 += it
        
        return s1 == s2
        