class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # print(f"n: {n}")
        
        if n == 1:
            return 0
        
        nums.sort()
        # print(nums)
        
        ans = nums[k - 1] - nums[0]
        # print(f"ans: {ans}")

        for i in range(k, n):
            first = i - k + 1
            # print(f"first: {first} second: {i}   ***  nums[first]: {nums[first]} nums[second]: {nums[i]}  **** nums[second] - nums[first]: {nums[i] - nums[first]} ")
            ans = min(ans, nums[i] - nums[first])
            
        return ans