def gauss(n):
    return (n * (n + 1)) // 2

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        temp = 0

        for i in range(n - 1):
            if nums[i] == 0:
                temp += 1
            
            if nums[i] != 0 and temp > 0:
                ans += gauss(temp)
                temp = 0
        
        if nums[n - 1] == 0:
            temp += 1
        
        if temp > 0:
            ans += gauss(temp)

        return ans