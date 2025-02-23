class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)
        freq = { }

        for it in nums:
            if it in freq:
                freq[it] += 1
            else:
                freq[it] = 1

        dist = 0

        for it in freq:
            if freq[it] > 2:
                return False
        
        return True