class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0

        n = len(words)

        # print(f"n: {n}")
        
        right = 1

        i = startIndex + 1
        if i >= n:
            i = 0
        
        while words[i] != target:
            if i == startIndex:
                return -1
            # print(i, words[i])
            i += 1
            right += 1
            if i >= n:
                i = 0
        
        # print(f"right: {right}")

        left = 1

        i = startIndex - 1
        if i < 0:
            i = n - 1
        
        while words[i] != target:
            # print(i, words[i])
            i -= 1
            left += 1
            if i < 0:
                i = n - 1
            
        # print(f"left: {left}")
            
        return min(left, right)

        
        