class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for it in mat:
            n = len(it)
            for i in range(n):
                if it[i] != it[(i + k) % n]:
                    return False
        
        return True
        