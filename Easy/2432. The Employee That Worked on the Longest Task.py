class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        st = 0
        ans = 9999
        time = -1

        for it in logs:
            tt = it[1] - st
            st = it[1]

            if tt > time or (tt == time and ans > it[0]):
                ans = it[0]
                time = tt
                
        return ans
        
        