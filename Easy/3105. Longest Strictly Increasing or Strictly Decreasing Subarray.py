class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1

        for i in range(n):
            inc = 1
            last = nums[i]

            for j in range(i + 1, n):
                if nums[j] > last:
                    inc += 1
                else:
                    break
                last = nums[j]
            
            dec = 1
            last = nums[i]
            for j in range(i + 1, n):
                if nums[j] < last:
                    dec += 1
                else:
                    break
                last = nums[j]

            # print(f"tot *** inc: {inc}, dec: {dec}")
            ans = max(ans, inc, dec)
        
        return ans
        