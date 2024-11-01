class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = { }
        ans = 0

        for it in nums:
            if it in dic:
                ans += dic[it]
                dic[it] += 1
            else:
                dic[it] = 1
        
        return ans
            

        