class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            n = len(nums)
            temp = []

            flag = True
            
            for i in range(0, n, 2):
                if flag: 
                    temp += [min(nums[i], nums[i + 1])]
                else:
                    temp += [max(nums[i], nums[i + 1])]
                
                flag = not flag
            
            nums = temp
        
        return nums[0]

        