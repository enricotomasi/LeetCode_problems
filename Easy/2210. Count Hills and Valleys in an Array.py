class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        
        arr = [nums[0]]

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                arr += [nums[i]]
        
        # print(arr)

        ans = 0
        n = len(arr)

        for i in range(1, n - 1):
            if (arr[i - 1] < arr[i] and arr[i + 1] < arr[i]) or (arr[i - 1] > arr[i] and arr[i + 1] > arr[i]):
                ans += 1

        return ans    
