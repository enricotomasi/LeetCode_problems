class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for it in intervals:
            sub = False
            for i in range(len(ans)):
                if (it[0] >= ans[i][0] and it[0] <= ans[i][1]) or (it[1] <= ans[i][1] and it[1] >= ans[i][0]):
                    sub = True
                    ans[i][0] = min(ans[i][0], it[0])
                    ans[i][1] = max(ans[i][1], it[1])
            
            if not sub:
                ans.append([it[0], it[1]])
        
        return ans