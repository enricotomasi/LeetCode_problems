class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = 50000000

        for i in range(n):
            temp = nums[i]
            if l == 1 and temp > 0:
                ans = min(ans, temp)
            # print(f"\n{nums[i]}")
            for j in range(i + 1, n):
                if j - i >= r:
                    break
                temp += nums[j]
                
                # print(f"{nums[j]}")
                
                if j - i + 1 >= l and temp > 0 :
                    ans = min(ans, temp)
                    # print(f" --> j - i >= l temp: {temp}, ans: {ans}")

        if ans == 50000000:
            return -1

        return ans
        