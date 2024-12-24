class Solution:
    def capitalizeTitle(self, title: str) -> str:
        st = title.split(" ")
        ans = []

        for it in st:
            
            if len(it) > 2:
                temp = it[0].upper()
                
                for i in range(1, len(it)):
                    temp += it[i].lower()
                
                ans += [temp]
            else:
                ans += [it.lower()]
            
        return ' '.join(ans)
