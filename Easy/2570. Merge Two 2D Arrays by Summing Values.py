class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = dict()

        for it in nums1:
            d[it[0]] = it[1]

        for it in nums2:
            if it[0] in d:
                d[it[0]] += it[1]
            else:
                d[it[0]] = it[1]
        
        ans = []

        for it in d:
            ans += [[it, d[it]]]

        ans.sort()

        return ans        
