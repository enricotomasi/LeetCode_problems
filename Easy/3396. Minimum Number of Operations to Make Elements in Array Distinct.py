class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = dict()

        for it in nums:
            if it in freq:
                freq[it] += 1
            else:
                freq[it] = 1
        
        # print(freq)
        
        n = len(nums)

        ok = True
        
        for it in freq:
            if freq[it] > 1:
                ok = False
                break
    
        if ok:
            return 0

        ans = 1
        for i in range(n):

            freq[nums[i]] -= 1

            # print(f"{i}#    {nums[i]}   ans: {ans}   --- {freq}")

            ok = True
            for it in freq:
                if freq[it] > 1:
                    ok = False
                    break
            
            if ok:
                # print(f"ok! ans: {ans}")
                return ans
            if (i + 1) % 3 == 0:
                ans += 1
            

        # print(f"ans: {ans}")
        return ans