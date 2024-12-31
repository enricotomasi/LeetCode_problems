class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        sc = [0 for _ in range(26)]

        for c in s:
            sc[ord(c) - ord('a')] += 1
        
        tc = [0 for _ in range(26)]

        for c in target:
            tc[ord(c) - ord('a')] += 1
        
        ans = 101

        for c in target:
            letter = ord(c) - ord('a')
            
            if sc[letter] <= 0:
                return 0
            
            m = sc[letter] // tc[letter]
            ans = min(ans, m)
                
        return ans
        
