class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []

        for it in nums:
            # print(it)
            if it in s:
                ans.append(it)
                if len(ans) == 2:
                    return ans
            else:
                s.add(it)
        
        return ans
        