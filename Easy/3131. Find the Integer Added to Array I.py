class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        nums1.sort()
        nums2.sort()

        ans = nums2[0] - nums1[0]
        
        for i in range(1, n):
            if nums2[i] - nums1[i] != ans:
                return -1
        
        return ans
