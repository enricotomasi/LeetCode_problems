def issorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0

        while True:
            # print(f"")
            if issorted(nums):
                return ans
            
            ans += 1

            mpos = -1
            msum = 99999999

            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < msum:
                    mpos = i
                    msum = nums[i] + nums[i + 1]

            # print(f"Couple: {mpos}, {mpos + 1} ### {nums[i]}, {nums[i + 1]} ### {msum}")
                            
            if mpos == 0:
                nums = [msum] + nums[2 : ]
                # print(f"mpos == 0             : {msum} + {nums[2 : ]}")
            elif mpos + 2 >= len(nums):
                nums = nums[0 : mpos] + [msum]
                # print(f"mpos + 2 >= len(nums) : {nums[0 : mpos]} + {msum}")
            else:
                nums = nums[0 : mpos] + [msum] + nums[mpos + 2 : ]
                # print(f"else                  : {nums[0 : mpos]} + {msum} + {nums[i + 2 : ]}")
            
            # print(nums)

        return ans
