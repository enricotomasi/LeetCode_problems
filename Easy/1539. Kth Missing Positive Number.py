class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ans = 1
        i = 0

        while i < n and k > 0:
            # print(f"{i}# arr[i]: {arr[i]}   ans: {ans} k: {k}")
            while (arr[i] != ans):
                if k == 1:
                    return ans
                ans += 1
                k -= 1
                # print(f" -> ans: {ans} k: {k}")
            
            i += 1
            ans += 1
        
        # print(f" exit -> ans: {ans} k: {k}")
        return ans + k - 1
        

        
            