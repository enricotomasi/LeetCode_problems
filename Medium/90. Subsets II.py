def rec(arr, temp, j, ans):
    
    ans.append(list(temp))
    n = len(arr)
    
    for i in range(j, n):
        if i > j and arr[i] == arr[i - 1]:
            continue
        
        temp.append(arr[i])
        
        rec(arr, temp, i + 1, ans)
        
        temp.pop()

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        rec(nums, [], 0, ans)
        
        return ans