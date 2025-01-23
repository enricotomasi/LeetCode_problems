class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(1, 10):
            if i in nums1 and i in nums2:
                return i
        
        m1 = 10
        for it in nums1:
            m1 = min(m1, it)
        
        m2 = 10
        for it in nums2:
            m2 = min(m2, it)

        ans = min(m1, m2) * 10 + max(m1, m2)

        return ans
        
