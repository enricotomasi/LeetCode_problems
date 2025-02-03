class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0

        if n == 1:
            if nums[0] % 2 == 0 and nums[0] <= threshold:
                return 1
            
            return 0
        
        for i in range(n):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                even = False
                temp = 1

                # print(f"\n{nums[i]} even")
                
                for j in range(i + 1, n):
                    # print(f"  --> {nums[j]} even: {even}")
                    if nums[j] > threshold:
                        break
                    if even: 
                        if nums[j] % 2 != 0:
                            break
                    else:
                        if nums[j] % 2 == 0:
                            break
                    
                    even = not even
                    temp += 1
                
                ans = max(ans, temp)

        return ans
        