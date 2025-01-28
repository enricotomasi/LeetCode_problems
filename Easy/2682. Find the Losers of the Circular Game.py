class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        pos = 0
        add = k

        ball = {}

        for i in range(n):
            ball[i] = 0
        
        ball[0] = 1
        
        while True:
            # print(f"\n{i}#")
            pos += add
            pos %= n

            add += k
            
            # print(f"pos: {pos}")
            
            if ball[pos] == 1:
                break

            ball[pos] += 1
        

        ans = []
        for it in ball:
            if ball[it] == 0:
                ans += [it + 1]

        return ans


