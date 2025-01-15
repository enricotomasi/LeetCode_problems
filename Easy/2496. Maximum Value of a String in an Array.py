class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = -1

        for it in strs:
            ele = -1
            if it.isnumeric():
                ele = int(it)
            else:
                ele = len(it)
            
            ans = max(ans, ele)
        
        return ans
        
