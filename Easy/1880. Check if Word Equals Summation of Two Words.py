def conv(s):
    ans = ""

    for c in s:
        ans += str(ord(c) - ord('a'))
    
    return int(ans)

class Solution:

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return conv(firstWord) + conv(secondWord) == conv(targetWord)
