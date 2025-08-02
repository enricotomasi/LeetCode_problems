class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        temp = 0
        temp2 = 0

        ans = 0

        for i in range(n - 1):    
            temp = max(temp, i + nums[i])

            if i == temp2:
                temp2 = temp
                ans += 1

        return ans