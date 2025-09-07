class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def rec(pos, temp):
            if len(temp) == k:
                ans.append(temp.copy())
                return
            
            for i in range(pos, n + 1):
                temp.append(i)
                rec(i + 1, temp)
                temp.pop()
        
        rec(1, [])
        return ans
        
