class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []

        while num:
            nums += [num % 10]
            num //= 10
            
        nums.sort()

        one = nums[0] * 10 + nums[3]
        two = nums[1] * 10 + nums[2]

        return one + two