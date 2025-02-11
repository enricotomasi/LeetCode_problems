def findmd(n):
    ans = -1

    while n > 0:
        ans = max(ans, n % 10)
        n //= 10

    return ans

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        dic = {}
        for i in range(10):
            dic[i] = []

        for it in nums:
            dic[findmd(it)] += [it]
        
        ans = -1

        for it in dic:
            lis = dic[it]
            n = len(lis)

            if n < 2:
                continue

            lis.sort()
            ans = max(ans, lis[n - 1] + lis[n - 2])

        return ans

        