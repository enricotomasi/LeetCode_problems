class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [False for i in range(51)]

        for it in ranges:
            for i in range(it[0], it[1] + 1):
                arr[i] = True
        
        for i in range(left, right + 1):
            if arr[i] != True:
                return False
        
        return True
        