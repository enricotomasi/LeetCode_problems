class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        ans1 = []
        for it in s1:
            if it not in s2:
                ans1 += [it]

        ans2 = []
        for it in s2:
            if it not in s1:
                ans2 += [it]
        
        return [ans1, ans2]
        
