def rec(i, n, d, temp, ans):
    if i >= n:
        if temp != "":
            ans += [temp]
        return ans
    
    for it in d[i]:
        rec(i + 1, n, d, temp + it, ans)
    
    return ans

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        d = []
    
        for i in range(n):
            d += [letters[ord(digits[i]) - ord('0')]]

        ans = rec(0, n, d, "", [])
               

        return ans