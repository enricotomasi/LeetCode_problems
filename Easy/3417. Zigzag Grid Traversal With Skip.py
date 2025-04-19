class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        flag1 = True
        flag2 = True
        ans = [ ]

        for i in range(m):
            if flag1:
                for j in range(n):
                    if flag2:
                        ans.append(grid[i][j])
                    flag2 = not flag2
            else:
                for j in range(n - 1, -1, -1):
                    if flag2:
                        ans.append(grid[i][j])
                    flag2 = not flag2

            flag1 = not flag1


        return ans  
