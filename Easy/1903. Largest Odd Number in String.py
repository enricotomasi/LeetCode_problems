class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        
        for i in range (n - 1, -1, -1):
            digit = ord(num[i]) - ord('0')
            if digit %2 != 0:
                return num[0 : i + 1]
        
        return ""
