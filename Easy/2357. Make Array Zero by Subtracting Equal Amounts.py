def rzero(arr):
    ans = []
    
    for it in arr:
        if it > 0:
            ans += [it]

    return ans


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        arr = rzero(nums)

        while len(arr) > 0:
            arr.sort()
            arr = rzero(arr)

            n = len(arr)
            if n == 0:
                return ans

            ans += 1
            
            remove = arr[0]

            for i in range(n):
                arr[i] -= remove

        return ans
