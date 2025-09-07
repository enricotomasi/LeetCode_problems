class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        def rec(pos, temp):
            if pos >= n:
                return
            
            rec(pos + 1, temp.copy())
            temp += [nums[pos]]
            rec(pos + 1, temp.copy())
            ans.append(temp.copy())
            temp.pop()

            
        ans.append([])
        for i in range(n):
            rec(i, [])

        temp = dict()
        for i in range(len(ans)):
            hash = ""
            for j in range(len(ans[i])):
                hash += str(ans[i][j])
                hash += '#'
            
            temp[hash] = ans[i]
        
        ans = []

        for it in temp:
            ans += [temp[it]]

        return ans