class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        ans = 1

        for i in range(n - 1):
            if word[i] == word[i + 1]:
                ans += 1
        
        return ans
          