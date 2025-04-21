class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = dict()
        
        for i in range(k):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1


        freq2 = dict()

        for it in freq:
            freq2[it] = 1
        
        # print(f"initizal freq2: {freq2}")

        for i in range(k, n):
            print(f"\n{i}# {nums[i]}")
            if freq[nums[i - k]] >= 1:
                freq[nums[i - k]] -= 1
            
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

            # print(f"freq: {freq}")
            
            for it in freq:
                # print(f"    -> {it}") 
                if freq[it] > 0:
                    if it in freq2:
                        # print(f"        -> add to freq2")
                        freq2[it] += 1
                    else:
                        freq2[it] = 1
                        # print(f"        -> set to freq2")
      
        ans = -1

        # print(f"\nfreq2 final: {freq2}")
        
        for it in freq2:
            if freq2[it] == 1:
                ans = max(ans, it)

        return ans