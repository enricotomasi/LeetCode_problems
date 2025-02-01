class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        idx = len(num) - 1

        while num[idx] == '0':
            idx -= 1

        return num [ : idx + 1]        