class Solution:
    def minMaxDifference(self, num: int) -> int:
        ns = str(num)
        n = len(ns)

        i = 0
        while i < n:
            if ns[i] != '9':
                break
            i += 1
        
        if i >= n:
            return num

        digitmax = ns[i]
        # print(f"digitmax: {digitmax}")

        # i = 0

        # while i < n:
        #     if ns[i] != '1':
        #         break
        #     i += 1
        
        digitmin = ns[0]
        # print(f"digitmin: {digitmin}")

        ansmax = ""

        for c in ns:
            if c == digitmax:
                ansmax += '9'
            else:
                ansmax += c
        
        ansmin = ""

        for c in ns:
            if c == digitmin:
                ansmin += '0'
            else:
                ansmin += c

        # print(f"ansmax: {ansmax} ansmin: {ansmin}")
        ans = int(ansmax) - int(ansmin)
        
        return ans