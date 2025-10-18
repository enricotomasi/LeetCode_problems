class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        
        last = -10 ** 15

        for it in nums:
            
            lo = it - k
            hi = it + k
            
            if last < lo:
                last = lo
            else:
                last += 1
            if last <= hi:
                ans += 1
            else:
                last -= 1

        return ans
