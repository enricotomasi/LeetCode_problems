class Solution:
    preans = []

    def rec(self, i, n, arr):
        if i == n:
            self.preans += [arr]

        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            self.rec(i + 1, n, arr[:])
            arr[i], arr[j] = arr[j], arr[i]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.preans = []
        self.rec(0, len(nums), nums)
        
        d = dict()
        
        for it in self.preans:
            toadd = ""
            for it2 in it:
                toadd += str(it2)
                toadd += "#"
            
            d[toadd] = it

        ans = []

        for it in d:
            ans += [d[it]]
        
        return ans
    
    
    
        