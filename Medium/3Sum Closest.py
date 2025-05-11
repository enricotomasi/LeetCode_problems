class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        diff = pow(9,32)

        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                
                if s < target:
                    j += 1
                else:
                    k -= 1
                
                if abs(s - target) < diff:
                    diff = abs(s - target)
                    ans = s
        
        return ans
        