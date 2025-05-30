class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        n = len(words)

        if words[0][0] != words[n - 1][len(words[n - 1]) - 1]:
            return False
        
        for i in range(n - 1):
            if (words[i][len(words[i]) - 1] != words[i + 1][0]):
                return False

        return True
        