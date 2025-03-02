class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        print(f"k: {k}")
        n = len(nums)
        ans = 500

        for i in range(n):
            for j in range(i + 1, n + 1):

                temp = nums[i]
                for q in range(i + 1, j):
                    #print(nums[k], end = " ")
                    temp |= nums[q]
                #print()
                # print("temp: ", temp, " ---- length:", j - i, "  ##### ", nums[i : j], end = "")
                if temp >= k:
                    ans = min(ans, (j - i))
                    # print(" ******** bingo!", end = "")
                print()
                    
        if ans > 499:
            return - 1

        return ans