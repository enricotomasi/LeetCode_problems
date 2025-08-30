class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path[0]
        
        for i in range(1, len(path)):
            if path[i - 1] == '/' and path[i] == '/':
                continue
            s += path[i]

        if s == '/':
            return s

        if s[len(s) - 1] == '/':
            s = s[ : len(s) - 1]

        # print(s)

        arr = s.split('/')

        # print(arr)

        st = []

        for i in range(1, len(arr)):
            if arr[i] == ".":
                continue
            elif arr[i] == "..":
                if len(st) > 0:
                    st.pop()
            else:
                st += [arr[i]]
            
        # print(st)

        if len(st) == 0:
            return "/"
        
        ans = "/"

        for it in st:
            ans += it
            ans += "/"

        return ans[ : -1 ]