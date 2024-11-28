def nice(s):
    upper = []
    lower = []

    for c in s:
        cl = c.lower()
        # print(cl)
        if c.isupper() and cl not in upper:
            # print(" -> upper")
            upper += [cl]
        elif not c.isupper() and c not in lower:
            # print(" -> lower")
            lower += [c]
    
    upper.sort()
    lower.sort()

    # print(len(upper), upper)
    # print(len(lower), lower)
    
    if len(upper) != len(lower):
        return False

    for i in range(len(upper)):
        # print(upper[i], lower[i])
        if upper[i] != lower[i]:
            return False
    
    return True

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
                
        n = len(s)
        ans = ""
        ml = 0

        for i in range(n):
            temp = s[i]
            for j in range(i + 1, n):
                temp += s[j]
                # print(f"*{temp}* {nice(temp)}")
                if len(temp) > len(ans) and nice(temp):
                    ans = temp
                    ml = len(ans)
        
        return ans
        
