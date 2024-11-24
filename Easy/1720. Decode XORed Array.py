class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        n = len(encoded)
        ans = [first]

        for i in range(n):
            ans += [encoded[i] ^ ans[i]]
        
        return ans
        


        