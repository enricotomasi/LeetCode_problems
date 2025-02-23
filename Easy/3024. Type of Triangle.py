class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] == nums[1] and nums[0] == nums[2] and nums[1] == nums[2]:
            return "equilateral"
        
        nums.sort()

        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        if nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"

        return "scalene"  