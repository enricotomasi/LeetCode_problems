class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        m = set()

        for i in range(n - 1):
            s = nums[i] + nums[i + 1]
            if s in m:
                return True
            m.add(s)

        return False