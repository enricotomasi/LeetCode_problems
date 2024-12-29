class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        last = [num[0], num[0], num[1]]
        ans = ""

        for i in range(2, n):
            last[0] = last[1]
            last[1] = last[2]
            last[2] = num[i]

            if (last[0] == last[1] and last[0] == last[2] and last[1] == last[2] and ans == "") or (last[0] == last[1] and last[0] == last[2] and last[1] == last[2] and ans[0] < last[0]):
                ans =  last[0] + last[0] + last[0]
        
        return ans
            


        
        