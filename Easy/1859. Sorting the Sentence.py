class Solution:
    def sortSentence(self, s: str) -> str:
        sent = s.split(" ")
        arr = [ "", "", "", "", "", "", "", "", "", "" ]

        for it in sent:
            index = ord(it[len(it) - 1]) - ord('0')
            arr[index - 1] = it[ : len(it) - 1]
        
        ans = ""

        ans = arr[0]

        for i in range(1, 10):
            if arr[i] != "":
                ans += " "
                ans += arr[i]

        return ans
