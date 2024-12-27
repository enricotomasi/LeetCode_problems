class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        indices = []

        for i in range(n):
            if nums[i] == key:
                indices += [i]
        
        # print(indices)

        preans = set()

        for it in indices:
            start = it - k
            end = it + k

            if start < 0:
                start = 0
            
            if end > n - 1:
                end = n - 1
            
            for i in range(start, end + 1):
                preans.add(i)
            
        
        ans = list(preans)
        ans.sort()

        return ans
