class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []

        for it in words:
            temp = ""
            for c in it:
                if c == separator:
                    if temp != "":
                        ans += [temp]
                    temp = ""
                else:
                    temp += c
            
            if temp != "":
                ans += [temp]

        return ans

        