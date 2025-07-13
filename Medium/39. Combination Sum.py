class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        def rec(i, s, temp):
            if s == target:
                ans.append(temp.copy())
                return
            
            if s > target or i >= n:
                return
            
            temp.append(candidates[i])
            rec(i, s + candidates[i], temp)
            temp.pop()
            rec(i + 1, s, temp)

            return ans

        return rec(0, 0, [])
        