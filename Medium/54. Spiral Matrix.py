class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        
        if m == 0:
            return []
        
        if m == 1:
            return matrix[0]
        
        n = len(matrix[0])

        ans = []

        xmin = 0
        xmax = m - 1 
        
        ymin = 0
        ymax = n - 1

        while (xmin <= xmax and ymin <= ymax):
            
            for i in range(ymin, ymax + 1):
                ans += [matrix[xmin][i]]
            xmin += 1

            for i in range(xmin, xmax + 1):
                ans += [matrix[i][ymax]]
            ymax -= 1

            if (xmin <= xmax):
                for i in range(ymax, ymin - 1, -1):
                    ans += [matrix[xmax][i]]
                xmax -= 1

            if (ymin <= ymax):
                for i in range(xmax, xmin - 1, -1):
                    ans += [matrix[i][ymin]]
                ymin += 1
        
        return ans