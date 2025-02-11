class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0

        for it in hours:
            if it >= target:
                ans += 1
        
        return ans
        