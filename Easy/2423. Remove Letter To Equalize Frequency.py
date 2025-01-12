def samefreq(word):
    freq = [0 for _ in range(26)]
        
    for c in word:
        freq[ord(c) - ord('a')] += 1
    
    value = -1
    
    for i in range(26):
        if freq[i] == 0:
            continue

        if value < 0:
            value = freq[i]
        elif value != freq[i]:
            return False
    
    return True

class Solution:
    def equalFrequency(self, word: str) -> bool:
        n = len(word)

        for i in range(n):
            newstring = word[: i] + word[i + 1: n]
            if samefreq(newstring):
                return True
        
        return False
                    