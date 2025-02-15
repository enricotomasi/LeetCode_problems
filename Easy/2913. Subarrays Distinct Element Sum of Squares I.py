class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            temp = set()
            temp.add(nums[i])
            ans += 1
            for j in range (i + 1, n):
                temp.add(nums[j])
                ans += len(temp) * len(temp)
        
        return ans