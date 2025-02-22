class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxdiag = -1
        maxarea = -1
        ans = 0

        for rect in dimensions:
            area = rect[0] * rect[1]
            diag = sqrt((rect[0] * rect[0]) + (rect[1] * rect[1]))

            if diag > maxdiag or diag == maxdiag and area > maxarea:
                ans = area
            
            maxdiag = max(maxdiag, diag)
            maxarea = max(maxarea, area)

        return ans