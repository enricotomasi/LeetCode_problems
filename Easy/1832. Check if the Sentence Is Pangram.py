class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = [ ]

        for c in sentence:
            if c not in d:
                d += [c]
        
        return len(d) == 26
        
