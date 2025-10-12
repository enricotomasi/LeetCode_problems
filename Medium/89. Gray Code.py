class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []

        for i in range(1 << n):
            ans += [ i ^ (i >> 1) ]
        
        return ans
        