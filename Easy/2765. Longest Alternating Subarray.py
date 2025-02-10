def check(arr):
    n = len(arr)
    
    # print(f"\n{arr} length: {n}")
    
    if n <= 1:
        return False
    
    last = -1

    for i in range(1, n):
        diff = arr[i] - arr[i - 1]
        # print(f"{i}# {arr[i]} - {arr[i - 1]} = {diff}  last: {last}")
        if diff == 1:
            if last != -1:
                return False
        elif diff == -1:
            if last != 1:
                return False 
        else:
            return False

        last = diff
    
    return True

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1

        for i in range(n):
            for j in range(i + 1, n):
                arr = nums[i : j + 1]
                              
                if check(arr):
                    # print(arr, "************* ", j - i + 1)
                    ans = max(ans, j - i + 1)
                # else:
                #     print(arr)
        
        return ans
