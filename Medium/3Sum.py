class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = []
       
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            x = nums[i]
            
            target = -x
            
            start = i + 1
            end = n - 1
            
            while start < end:
                current_sum = nums[start] + nums[end]
                if current_sum == target:
                    ans.append([x, nums[start], nums[end]])
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    start += 1
                    end -= 1
                elif current_sum < target:
                    start += 1
                else:
                    end -= 1
        
        return ans