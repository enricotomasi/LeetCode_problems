class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        ans = []

        last = 15

        for i in range(n):
            if groups[i] != last:
                ans += [words[i]]
            
            last = groups[i]
        
        return ans       