class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        s = set()
        ans = 0

        for it in words:
            rev = it[ : : -1 ]
            if rev in s:
                ans += 1
            else:
                s.add(it)
        
        return ans