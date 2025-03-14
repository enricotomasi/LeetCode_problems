class Solution:
    def getSmallestString(self, s: str) -> str:
        arr = list(s)
        n = len(s)

        for i in range(0, n - 1):
            first = ord(arr[i]) - ord('0')
            second = ord(arr[i + 1]) - ord('0')

            if ((first % 2 == 0 and second % 2 == 0) or (first % 2 != 0 and second % 2 != 0)) and first > second:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                break
        
        return "".join(arr)