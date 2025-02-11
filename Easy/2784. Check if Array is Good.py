class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()

        # print(f"n: {n}")
        print(nums)

        for i in range(n - 1):
            # print(f" -> {i}# {nums[i]}")
            if nums[i] != i + 1:
                # print(" -> Exit!")
                return False
        
        # print(f"{nums[n - 1]}")
        return nums[n - 1] == n - 1