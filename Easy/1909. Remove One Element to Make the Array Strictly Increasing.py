class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            ok = True

            arr = list(nums)
            arr.pop(i)

            for i in range(1, n - 1):
                if arr[i - 1] >= arr[i]:
                    ok = False
                    break

            if ok:
                return True
        
        return False

            