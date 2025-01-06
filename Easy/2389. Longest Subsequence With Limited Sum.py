class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        tot = 0
        for it in nums:
            tot += it
        
        ans = []

        for it in queries:
            if it > tot:
                ans += [n]
                continue
            
            temp = 0
            count = 0

            for it2 in nums:
                if temp + it2 > it:
                    break
                temp += it2
                count += 1
            
            ans += [count]

        return ans