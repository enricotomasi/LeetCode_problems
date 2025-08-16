class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        top = 0

        for i in range(n):
            if top < i:
                return False
            
            top = max(i + nums[i], top)
        
        # print(f"top: {top}")
        return top >= n - 1
