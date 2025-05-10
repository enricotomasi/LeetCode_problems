class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = 0
        zero1 = 0

        for it in nums1:
            if it == 0:
                zero1 += 1
            else:
                sum1 += it
        
        # print(f"sum1: {sum1} zero1: {zero1}")

        sum2 = 0
        zero2 = 0

        for it in nums2:
            if it == 0:
                zero2 += 1
            else:
                sum2 += it
        
        # print(f"sum2: {sum2} zero2: {zero2}")

        if (zero1 == 0 and (sum2 + zero2) > sum1) or (zero2 == 0 and (sum1 + zero1) > sum2):
            return -1

        return max(sum1 + zero1, sum2 + zero2)