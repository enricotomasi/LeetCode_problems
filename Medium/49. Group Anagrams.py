class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for word in strs:
            w = list(word)
            w.sort()
            key = "".join(w)
            if key in d:
                d[key] += [word]
            else:
                d[key] = [word]
        
        #print(d)
        
        ans = []

        for it in d:
            ans += [d[it]]
        
        return ans
        