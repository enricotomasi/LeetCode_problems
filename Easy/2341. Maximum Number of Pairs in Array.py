class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0 for _ in range(101)]

        for it in nums:
            freq[it] += 1
        
        ans0 = 0

        for i in range(101):
            if freq[i] > 0:
                ans0 += freq[i] // 2
        
        return [ans0, (n - (ans0 * 2))]
        
        