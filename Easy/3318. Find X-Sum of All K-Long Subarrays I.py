def xsum(arr, x):
    dic = dict()

    for it in arr:
        if it in dic:
            dic[it] += 1
        else:
            dic[it] = 1
    
   
    dic = dict(sorted(dic.items(), key = lambda item: item[0], reverse = True))
    dic = dict(sorted(dic.items(), key = lambda item: item[1], reverse = True))

    i = 0
    ans = 0
    
    for it in dic:
        i += 1
        if i > x:
            break
        ans += it * dic[it]
        # print(f"  -->  {i}# {it} * {dic[it]} = {it * dic[it]}    ans: {ans}")
    
    return ans

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0 for _ in range(n - k + 1)]

        for i in range(n - k + 1):
            end = i + k
            # print(f"\n{i}# {nums[i : end]}")
            ans[i] = xsum(nums[i : end], x)
            # print(ans[i])
        
        return ans
