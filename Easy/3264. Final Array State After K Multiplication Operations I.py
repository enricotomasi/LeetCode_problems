import sys

def findmin(arr, n):
    ans = -1
    m = sys.maxsize

    for i in range(n):
        if arr[i] < m:
            m = arr[i]
            ans = i
    
    return ans


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        
        for i in range(k):
            # print(nums, findmin(nums, n))
            nums[findmin(nums, n)] *= multiplier

        return nums