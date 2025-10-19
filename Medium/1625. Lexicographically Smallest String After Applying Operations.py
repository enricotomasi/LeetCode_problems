from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        
        visited = set([s])
        queue = deque([s])
        
        while len(queue) > 0:
            temp = queue.pop()
            
            if temp < ans:
                ans = temp
            
            digits = list(temp)

            for i in range(1, len(s), 2):
                digits[i] = str((int(digits[i]) + a) % 10)

            digits2 = ''.join(digits)
            
            if digits2 not in visited:
                visited.add(digits2)
                queue.append(digits2)
            
            new = temp[ -b : ] + temp[ : - b ]
            
            if new not in visited:
                visited.add(new)
                queue.append(new)
        
        return ans