class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 5000

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    for k in range(j + 1, n):
                        if nums[k] < nums[j]:
                            #  print(i, j, k, "******", nums[i], nums[j], nums[k])
                             ans = min(ans, (nums[i] + nums[j] + nums[k]))
        
        if ans == 5000:
            return -1

        return ans
        