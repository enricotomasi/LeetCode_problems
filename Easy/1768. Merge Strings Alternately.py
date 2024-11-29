class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)

        i = 0
        j = 0

        ans = ""
        flag = True

        while i < n1 or j < n2:
            if flag:
                if i < n1:
                    ans += word1[i]
                    i +=1
            else:
                if j < n2:
                    ans += word2[j]
                    j += 1
            
            flag = not flag
        
        return ans
            

        
