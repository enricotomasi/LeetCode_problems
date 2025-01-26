class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = -1
        d = -1

        for div in divisors:
            temp = 0
            for num in nums:
                if num % div == 0:
                    temp += 1
            
            if temp > ans or (temp == ans and div < d):
                ans = temp
                d = div
        
        return d
            