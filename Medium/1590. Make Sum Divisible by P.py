class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        ans = n
        tot = sum(nums)

        if tot % p == 0:
            return 0

        remove = tot % p
        temp = 0

        m = {0: -1}

        for i in range(n):
            temp = (temp + nums[i]) % p
            temp2 = (temp - remove) % p
            
            if temp2 in m:
                ans = min(ans, i - m[temp2])

            m[temp] = i

        if ans < n:
            return ans
        
        return -1



