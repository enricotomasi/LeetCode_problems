class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        
        l1 = list(s)

        l2 = []

        for it in words:
            l2 += [ it[0] ]

        n = len(l1)

        for i in range(n):
            if l1[i] != l2[i]:
                return False
        
        return True     