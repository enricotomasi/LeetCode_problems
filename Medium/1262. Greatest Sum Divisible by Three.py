class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)

        if s % 3 == 0:
            return s

        nums.sort()
        temp = 0
        temp1 = 0

        if s % 3 == 2:
            for i in nums:
                if i % 3 == 2:
                    if temp1 == 2:
                        return s - min(i, temp)
                    return s - i
                elif i % 3 == 1 and temp1 < 2:
                    temp += i
                    temp1 += 1
        else:
            for i in nums:
                if i % 3 == 1:
                    if temp1 == 2:
                        return s - min(i, temp)
                    return s - i
                elif i % 3 == 2 and temp1 < 2:
                    temp += i
                    temp1 += 1

        if temp1 != 2:
            return s

        return s - temp

