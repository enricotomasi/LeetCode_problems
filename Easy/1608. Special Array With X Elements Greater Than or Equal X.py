class Solution:

    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i in range(1, n + 1):
            c = 0
            
            for j in range(n - 1, -1, -1):
                if nums[j] >= i:
                    c += 1
                else:
                    break
            
            if c == i:
                return c
        
        return -1
