class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = nums[0]
        
        for i in range(1, n):
            arr = nums[i]
            temp = []

            for it in arr:
                if it in ans:
                    temp += [it]
            
            ans = temp

        ans.sort()
        return ans
        