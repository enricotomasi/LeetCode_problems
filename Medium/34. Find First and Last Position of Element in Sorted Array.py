class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        if n == 0:
            return [ -1, -1 ]

        if n == 1:
            if nums[0] == target:
                return [ 0, 0 ]
            else:
                return [ -1, -1 ]
        
        start = 0
        end = n - 1
        pivot = -1

        while start <= end:
            pivot = (start + end) // 2
            # print(pivot)
            if nums[pivot] == target:
                break
            elif nums[pivot] > target:
                end = pivot - 1
            else:
                start = pivot + 1
        
        if nums[pivot] != target:
            return [ -1, -1 ]
        
        posinf = pivot
        while (posinf >= 0 and nums[posinf] == target):
            # print(posinf, nums[posinf])
            posinf -= 1
        
        posinf += 1


        possup = pivot
        while (possup < n and nums[possup] == target):
            # print(possup, nums[possup])
            possup += 1

        possup -= 1


        return [posinf, possup]

                