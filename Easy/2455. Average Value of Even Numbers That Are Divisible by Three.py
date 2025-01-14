class Solution:
    def averageValue(self, nums: List[int]) -> int:
        div = []

        for it in nums:
            if it %2 == 0 and it % 3 == 0:
                div += [it]

        tot = 0

        for it in div:
            tot += it
        
        if len(div) == 0:
            return 0

        return tot // len(div)
        
