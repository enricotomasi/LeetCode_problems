class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        arr = [" " for _ in range(n)]

        for i in range(n):
            arr[indices[i]] = s[i]
        
        ans = ""
        
        for it in arr:
            ans += it

        return ans


            
        