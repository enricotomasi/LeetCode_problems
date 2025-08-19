class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        ins = 1

        right = 0
        left = n - 1

        up = 0
        down = n - 1

        while right <= left and up <= down:
            # print(f"\nleft: {left} right: {right} down: {down} up: {up}")
            # print("right")
            for i in range(right, left + 1):
                # print(i)
                ans[up][i] = ins
                ins += 1
            up += 1
            
            # print(ans)

            # print(f"\nleft: {left} right: {right} down: {down} up: {up}")
            # print("down")
            for i in range(up, down + 1):
                # print(i)
                ans[i][left] = ins
                ins += 1
            left -= 1

            # print(ans)

            # print(f"\nleft: {left} right: {right} down: {down} up: {up}")
            # print("left")
            for i in range(left, right - 1, -1):
                # print(i)
                ans[down][i] = ins
                ins += 1
            down -= 1

            # print(ans)

            # print(f"\nleft: {left} right: {right} down: {down} up: {up}")
            # print("up")
            for i in range(down, up - 1, - 1):
                # print(i)
                ans[i][right] = ins
                ins += 1
            right += 1
            
            # print(ans)
        
        return ans