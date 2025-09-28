class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # print(f"n: {n}")
        
        used1 = set()
        used2 = set()

        offset = 0
        i = 0

        while i + offset < n:
            nums[i] = nums[i + offset]

            if nums[i] in used1:
                if nums[i] in used2:
                    offset += 1
                else:
                    used2.add(nums[i])
                    i += 1
            else:
                used1.add(nums[i])
                i += 1

        for i in range(offset):
            nums.pop()