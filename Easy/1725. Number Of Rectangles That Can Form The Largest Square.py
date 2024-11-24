class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = []

        for it in rectangles:
            arr += [min(it[0], it[1])]
        
        arr.sort(reverse = True)

        m = arr[0]
        ans = 0

        for it in arr:
            if it == m:
                ans += 1
            else:
                break
        
        return ans

        
        