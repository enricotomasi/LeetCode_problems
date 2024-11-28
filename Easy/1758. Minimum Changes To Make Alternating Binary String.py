def check(s, n, ans, last):
    for i in range(1, n):
            if s[i] == last:
                ans += 1
                if (s[i] == "1"):
                    last = "0"
                else:
                    last = "1"
            else:
                last = s[i]
    return ans

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        last = s[0]
        ans0 = check(s, n, 0, last)
        
        if s[0] == "0":
            last = "1"
        else:
            last = "0"
        
        ans1 = check(s, n, 1, last)

        return min(ans0, ans1)
               
