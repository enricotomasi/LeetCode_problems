class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)

        # print(f"n: {n}")

        po = -1
        pn = -1

        for i in range(n):
            if nums[i] == 1:
                po = i
                if pn > 0:
                    break
            elif nums[i] == n:
                pn = i
                if po > 0:
                    break
            # print(f"  --->  {i}#   _{nums[i]}_   po: {po} pn: {pn}")
        
        # print(f"po: {po} pn: {pn}")

        if po < pn:
            return po + (n - pn - 1)
        else:
            return po + (n - pn - 1) - 1
        


      