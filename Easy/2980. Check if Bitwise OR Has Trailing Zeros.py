class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                # print(f"{i}, {j}   {nums[i]} | {nums[j]} = {nums[i] | nums[j]}")
                if (nums[i] | nums[j]) % 2 == 0:
                    return True
        
        return False
        