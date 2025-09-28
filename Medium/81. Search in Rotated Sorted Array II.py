def bs(arr, start, end, target):
    while start <= end:
        pivot = (start + end) // 2
        if arr[pivot] == target:
            return True
        elif arr[pivot] > target:
            end = pivot - 1
        else:
            start = pivot + 1
    
    return False
    

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        step = n // 10
        rot = -1
        i = 0

        if n == 1:
            return nums[0] == target

        if step > 0:
            while i + step < n:
                if nums[i] > nums[i + step]:
                    break
                i += step

        for i in range(rot, n - 1):
            if nums[i + rot] > nums[i + rot + 1]:
                rot += i + 1
                break
        
        return bs(nums, 0, rot - 1, target) or bs(nums, rot, n - 1, target)