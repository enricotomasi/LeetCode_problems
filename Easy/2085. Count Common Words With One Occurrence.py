class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        m1 = { }
        for it in words1:
            if it in m1:
                m1[it] += 1
            else:
                m1[it] = 1
        
        m2 = { }
        for it in words2:
            if it in m2:
                m2[it] += 1
            else:
                m2[it] = 1
        
        ans = 0

        for it in m1:
            if m1[it] == 1 and it in m2 and m2[it] == 1:
                ans += 1

        return ans
