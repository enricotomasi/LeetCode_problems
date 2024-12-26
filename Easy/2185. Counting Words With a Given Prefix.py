class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pn = len(pref)
        ans = 0

        for it in words:
            n = len(it)

            
            if it[0] != pref[0]:
                continue
            
            i = 1
            j = 1
            
            while i < n and j < pn:
                if it[i] != pref[j]:
                    break
                i += 1
                j += 1
            
            # print(f"{pref} {it}   {j >= pn -1}   {ans}")

            if j >= pn:
                ans += 1
        
        return ans
        {\rtf1}