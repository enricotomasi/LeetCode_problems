class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        br = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                br = i
                break
        
        if br < 0:
            nums.reverse()
            return
        
        for i in range(n - 1, br, -1):
            if nums[i] > nums[br]:
                nums[i], nums[br] = nums[br], nums[i]
                break

        nums[br + 1 : ] = reversed(nums[br + 1 : ])