class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        ans = ""
        arr = [[] for _ in range(numRows)]
        mid = numRows // 2
        
        long = True

        pos = 0

        while pos < n:
            if long:
                for i in range(numRows):
                    if pos >= n:
                        break
                    arr[i].append(s[pos])
                    pos += 1
            else:
                # arr[0].append("")
                # arr[numRows - 1].append("")
                for i in range(numRows - 2, 0, - 1):
                    if pos >= n:
                        break
                    arr[i].append(s[pos])
                    pos += 1
            
            long = not long
    
        
        # for it in arr:
        #     print(it)

        ans = ""

        for i in range(numRows):
            for it in arr[i]:
                ans += it

        return ans