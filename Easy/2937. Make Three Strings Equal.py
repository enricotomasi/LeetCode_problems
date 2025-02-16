class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        ml = min(len(s1), len(s2), len(s3))
        com = ml
        
        for i in range(ml):
            if s1[i] != s2[i] or s1[i] != s3[i] or s2[i] != s3[i]:
                com = i
                break

        if com == 0:
            return -1
        
        return len(s1) + len(s2) + len(s3) - (com * 3)
        