class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        m1 = [0 for _ in range(26)]

        for c in word1:
            m1[ord(c) - ord('a')] += 1

        # print(m1)

        m2 = [0 for _ in range(26)]

        for c in word2:
            m2[ord(c) - ord('a')] += 1

        # print(m2)

        jolly = 3

        for i in range(26):
            if abs(m1[i] - m2[i]) > jolly:
                return False

        return True