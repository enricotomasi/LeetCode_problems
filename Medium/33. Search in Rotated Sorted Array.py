def bs(arr, target, start, end):
    while start <= end:
        pivot = (start + end) // 2
        if arr[pivot] == target:
            return pivot
        elif arr[pivot] > target:
            end = pivot - 1
        else:
            start = pivot + 1
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n < 10:
            for i in range(n):
                if nums[i] == target:
                    return i
            return - 1
        
        step = 10
        start = 0

        while start <= n - step - 1:
            end = start + step
            if nums[start] > nums[end]:
                break
            
            start += step
        
        # print(f"nums[start]: {nums[start]}")

        # start -= min(0, start - step)
        pivot = min(start + step, n -1)
        for i in range(start, min(n - 1, start + step)):
            if nums[i - 1] > nums [i]:
                pivot = i
                break

        # print(f"pivot: {pivot} = {nums[pivot]}")        
        
        # print(nums[ :  pivot])
        # print(nums[pivot : n - 1])

        ans = bs(nums, target, 0, pivot)

        if ans >= 0:
            return ans
        
        ans = bs(nums, target, pivot, n - 1)
        
        return ans
