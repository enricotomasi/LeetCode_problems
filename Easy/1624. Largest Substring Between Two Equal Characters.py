class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        ans = -1

        for i in range(26):
            c = " "
            c = chr(ord('a') + i)
            
            start = 0
            end = 0

            flag = True

            for i in range(n):
                if (c == s[i]):
                    if flag:
                        start = i
                        flag = False
                    else:
                        end = i
                ans = max(ans, (end - start - 1))

        return ans
        
        
