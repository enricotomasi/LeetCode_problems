class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        n1 = set()
        for it in nums1:
            n1.add(it)
        
        n2 = set()
        for it in nums2:
            n2.add(it)
        
        n3 = set()
        for it in nums3:
            n3.add(it)
        
        ans = set()

        for it in nums1:
            if it in n2 or it in n3:
                ans.add(it)
        
        for it in nums2:
            if it in n1 or it in n3:
                ans.add(it)
        
        return list(ans)
        