def bs(arr, tofind, start, end):
    # print(f"\nbs {arr} tofind: {tofind}, start: {start}, end: {end}")
    
    while start <= end:
        mid = (start + end) // 2
        # print(f"  -> mid: {mid} start: {start}, end: {end}")
        if arr[mid] == tofind:
            # print("ok find, exit\n")
            return mid
        elif arr[mid] > tofind:
            end = mid - 1
        else:
            start = mid + 1
    
    # print("not found, exit\n")
    return -1


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = len(nums)
        
        if n == 1:
            if nums[0] == original:
                return original * 2
            else:
                return original
        
        nums.sort()

        if bs(nums, original, 0, n) < 0:
            return original

        ans = original

        start = 0

        while start < n:
            start = bs(nums, ans * 2, start, n - 1)
            # print(ans * 2, start)
            if start < 0:
                return ans * 2
            
            ans *= 2

        return -1
