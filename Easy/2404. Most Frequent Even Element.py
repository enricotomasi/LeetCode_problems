class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        m = { }

        for it in nums:
            if it % 2 == 0:
                if it in m:
                    m[it] += 1
                else:
                    m[it] = 1
        
        if (len(m) == 0):
            return -1

        ans = 1000000000
        freq = -1
        
        for it in m:
            if m[it] > freq:
                freq = m[it]
                ans = it
            elif m[it] == freq and it < ans:
                ans = it
        
        return ans