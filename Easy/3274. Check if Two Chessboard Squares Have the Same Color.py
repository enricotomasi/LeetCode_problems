class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c11 = ord(coordinate1[0]) - ord('a')
        c12 = ord(coordinate1[1]) - ord('0')

        c21 = ord(coordinate2[0]) - ord('a')
        c22 = ord(coordinate2[1]) - ord('0')

        # print(c11, c12)
        # print(c21, c22)

        a = c11 % 2 == c12 % 2
        b = c21 % 2 == c22 % 2

        return a == b
