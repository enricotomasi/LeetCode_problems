class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        first = [-1 for _ in range(26)]
        
        for i in range(n):
            letter = ord(s[i]) - ord('a')
            if first[letter] < 0:
                first[letter] = i
            else:
                dist = i - first[letter] - 1
                if dist != distance[letter]:
                    return False

        return True
        