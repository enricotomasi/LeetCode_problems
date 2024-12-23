class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)

        # print(f"n: {n}")
        
        m = { }

        for i in range(101):
            m[i] = [0, 0, 0]


        for i in range(0, n, 2):
            pos = ord(rings[i + 1]) - ord('0')
            if rings[i] == 'R':
                m[pos][0] = 1
            elif rings[i] == 'G':
                m[pos][1] = 1
            else:
                m[pos][2] = 1
        
        # print(m)
        ans = 0

        for it in m:
            if m[it][0] == 1 and m[it][1] == 1 and m[it][2] == 1:
                ans += 1
        
        return ans

        
        
