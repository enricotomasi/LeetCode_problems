class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [ 0 for _ in range(101)]

        for it in nums:
            freq[it] += 1
        
        mf = -1

        for it in freq:
            mf = max(mf, it)
        
        ans = 0

        for it in freq:
            if it == mf:
                ans += mf
        
        return ans