def check(arr):
    n = len(arr)
    
    last = - 1
    
    for i in range(n):
        if last >= arr[i]:
            return False
        last = arr[i]
    
    return True

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                # print(f"\n{i}, {j}")
                # print(nums[i : j])
                # print(arr)
                arr = nums[ : i ] + nums [ j : ]
                if check(arr):
                    ans += 1
        
        return ans