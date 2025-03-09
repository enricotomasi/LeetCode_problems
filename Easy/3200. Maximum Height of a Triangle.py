def tr(r, b, flag):
    ans = 1
    while True:
        if flag:
            if r - ans < 0:
                break
            else:
                r -= ans
        else:
            if b - ans < 0:
                break
            else:
                b -= ans

        # print(f"r: {r}, b: {b}, ans: {ans}")
        flag = not flag
        ans += 1
    
    return ans - 1
        

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(tr(red, blue, True), tr(red, blue, False))