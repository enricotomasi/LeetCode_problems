class Solution:
    def slowestKey(self, r: List[int], k: str) -> str:
        n = len(r)
        ans = k[0]
        m = r[0]

        # print(f"m: {m}, ans: {ans}")

        for i in range(1, n):
            t = r[i] - r[i - 1]
            # print(f"{i}# {r[i]} {k[i]}  *** {r[i]} - {r[i - 1]} = {r[i] - r[i - 1]}  *** m: {m}, ans: {ans}")
            if t > m or (t == m and ord(k[i]) > ord(ans)):
                m = t
                ans = k[i]

        
        return ans
        
