class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg = set()
        pos = set()

        for it in nums:
            if it < 0:
                neg.add(it)
            else:
                pos.add(it)
        
        ans = -1

        for it in pos:
            if it * -1 in neg and it > ans:
                ans = it
        
        return ans
        
