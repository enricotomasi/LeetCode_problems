class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        j = n - 1

        ans = 0

        while i < j:
            # print(f"\nnums[{i}]: {nums[i]} nums[{j}]: {nums[j]}")
            
            toadd = nums[j]
            temp = nums[i]
            
            p = int(log10(toadd)) + 1
            # print(f"p: {p}")

            while temp > 0:
                digit = temp % 10
                toadd += pow(10, p) * digit
                temp //= 10
                # print(f" ---> digit: {digit} temp: {temp} p: {p}")
                p += 1

            # print(f"toadd: {toadd}")
            ans += toadd

            i += 1
            j -= 1

        if i == j:
            ans += nums[i]
        
        return ans

        
        