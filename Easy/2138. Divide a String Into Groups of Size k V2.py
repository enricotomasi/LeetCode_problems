class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        temp = ""
        cnt = 0

        for c in s:
            cnt += 1
            temp += c

            if cnt == k:
                ans.append(temp)
                temp = ""
                cnt = 0
        
        if temp != "":
            if len(temp) != k:
                for i in range(k - len(temp)):
                    temp += fill
                
            ans.append(temp)


        return ans

        