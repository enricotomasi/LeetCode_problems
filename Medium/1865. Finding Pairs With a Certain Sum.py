class FindSumPairs:

    n1 = []
    n2 = []
    freq = dict()
    
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.freq = dict()
        
        for it in nums2:
            if it in self.freq:
                self.freq[it] += 1
            else:
                self.freq[it] = 1

    def add(self, index: int, val: int) -> None:
        old = self.n2[index]

        self.n2[index] += val

        if self.freq[old] > 0:
            self.freq[old] -= 1
        
        if self.n2[index] in self.freq:
            self.freq[self.n2[index]] += 1
        else:
            self.freq[self.n2[index]] = 1

    def count(self, tot: int) -> int:
        d = dict()

        ans = 0 
        
        for it1 in self.n1:
            if tot - it1 in self.freq:
                ans += self.freq[tot - it1]

        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)