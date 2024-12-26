class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        
        m = { }

        for i in range(n - 1):
            if nums[i] == key:
                if nums[i + 1] in m:
                    m[nums[i + 1]] += 1
                else:
                    m[nums[i + 1]] = 1
        
        # print(m)
        c = -1
        ans = -1

        for it in m:
            if m[it] > c:
                c = m[it]
                ans = it
                
        return ans
        