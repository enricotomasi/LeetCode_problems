def bs(arr, n, target):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    
    return False

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        
        for it in nums1:
            if bs(nums2, n, it):
                return it

        return -1     
