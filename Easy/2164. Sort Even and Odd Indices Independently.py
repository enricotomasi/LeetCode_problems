class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)

        even = []
        odd = []

        for i in range(n):
            if i % 2 == 0:
                 even += [nums[i]]
            else:
                odd += [nums[i]]

        even.sort()
        odd.sort(reverse = True)

        print(even)
        print(odd)

        ans = []

        j = 0
        k = 0

        for i in range(n):
            if i % 2 == 0:
                ans += [even[j]]
                j += 1
            else:
                ans += [odd[k]]
                k += 1
        
        return ans

        

        