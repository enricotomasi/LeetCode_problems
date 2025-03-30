class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # print(f"n: {n} k: {k}  n - (k * 2) + 1: {n - (k * 2) + 1}")

        if n <= 3 or k == 1:
            return True

        for i in range(n - (k * 2) + 1):
            # print(f"\n{i}#")
            inc = True
            
            for j in range(k - 1):
                # print(f" 1   -> {j}# {nums[i + j + 1]} <= {nums[i + j]}")
                if nums[i + j + 1] <= nums[i + j]:
                    inc = False
                    break

            if not inc:
                # print("non inc, continue")
                continue

            for j in range(k - 1):
                # print(f" 2   -> {j}# {nums[i + j + k + 1]} <= {nums[i + j + k]}")
                if nums[i + j + k + 1] <= nums[i + j + k]:
                    inc = False
                    break

            if inc:
                return True
        
        # print(" *** false *** end")
        return False