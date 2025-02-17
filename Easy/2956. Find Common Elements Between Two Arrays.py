class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        ans1 = 0
        for it in nums1:
            if it in s2:
                ans1 += 1
        
        ans2 = 0
        for it in nums2:
            if it in s1:
                ans2 += 1

        return [ans1, ans2]     
