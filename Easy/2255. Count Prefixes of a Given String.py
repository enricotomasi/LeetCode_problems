class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        n = len(s)

        for it in words:
            # print(f"\n{it} len(it): {len(it)}")
            if it[0] != s[0]:
                # print("First letter different, exit!")
                continue
                        
            ni = len(it)
            
            i = 0
            j = 0
            
            while i < ni and j < n:
                # print(f"i: {i} j: {j} it[i]: {it[i]} s[j]: {s[j]}")
                if it[i] != s[j]:
                    break
                
                i += 1
                j += 1
            
            print(f"i: {i}")
            if i == ni:
                # print("Bingo!")
                ans += 1
        
        return ans
        