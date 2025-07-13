class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        temp = []

        def rec(i, c):
            if c == 0:
                ans.append(temp.copy())
                return
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] > c:
                    break
                temp.append(candidates[j])
                rec(j + 1, c - candidates[j])
                temp.pop()

        rec(0, target)
        
        return ans