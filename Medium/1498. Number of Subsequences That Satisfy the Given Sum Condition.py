class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        m = pow(10, 9) + 7
        n = len(nums)
        nums.sort()  
        
        ans = 0
        start = 0
        end = n - 1

        while start <= end:
            if nums[start] + nums[end] <= target:
                ans = (ans + pow(2, (end - start))) % m
                start += 1  
            else:
                end -= 1  
                
        return ans