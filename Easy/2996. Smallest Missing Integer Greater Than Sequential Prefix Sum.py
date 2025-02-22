class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0] + 1

        longest = nums[0]
        temp = nums[0]

        s = set()
        s.add(nums[0])
        for i in range(1, n):
            s.add(nums[i])
            if nums[i - 1] == nums[i] - 1:
                temp += nums[i]
            else:
                temp = 0
            longest = max(longest, temp)
        
        if nums[0] != nums[1] - 1:
            longest = nums[0]
        
        # print(f"Longest: {longest}")

        while True:
            if longest not in s:
                return longest
            
            longest += 1

        return -1
       