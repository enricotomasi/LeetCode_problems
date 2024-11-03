class Solution:
    def makeGood(self, s: str) -> str:
        changes = 1000
        
        while changes > 0:
            # print()
            changes = 0

            for i in range(len(s) - 1):
                # print(f"{i}# len(s): {len(s)}")
                if (s[i].isupper() and s[i + 1].islower()) or (s[i].islower() and s[i + 1].isupper()):
                    if (s[i].lower() == s[i + 1].lower()):
                        changes += 1
                        s = s[0 : i] + s[i + 2 : ]
                        break
                
                # print(f" --> s: {s}")
            
            # print(f"changes: {changes}")
        
        return s
            
        