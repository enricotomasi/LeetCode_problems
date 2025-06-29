class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            arrrow = [0 for _ in range(10)]
            arrcol = [0 for _ in range(10)]
            # print("\n*************")
            for j in range(9):
                print(board[j][i])
                if board[i][j] != ".":
                    arrrow[ord(board[i][j]) - ord('0')] += 1
                
                if board[j][i] != ".":
                    arrcol[ord(board[j][i]) - ord('0')] += 1
                # print(arrrow)
                # print(arrcol)
            
            # print("*************")
            # print(arrrow)
            # print(arrcol)
                
            for j in range(10):
                if arrrow[j] > 1 or arrcol[j] > 1:
                    return False
        
        for i in range(3):
            for j in range(3):
                addx = i * 3
                addy = j * 3

                # print()
                arrsquare = [0 for _ in range(10)]

                for k in range(3):
                    for l in range(3):
                        x = addx + k
                        y = addy + l
                        # print(x, y, "*****", board[x][y])
                        if board[x][y] != '.':
                            arrsquare[ord(board[x][y]) - ord('0')] += 1
                
                # print(arrsquare)
                for k in range(10):
                    if arrsquare[k] > 1:
                        return False

        return True
