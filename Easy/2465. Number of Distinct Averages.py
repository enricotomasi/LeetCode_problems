class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        arr1 = nums[ : n // 2]
        arr2 = nums[(n // 2) :]
        
        s = set()

        for i in range(n // 2):
            avg = (arr1[i] + arr2[(n // 2) - i - 1]) / 2
            s.add(avg)

        return len(s)
        
