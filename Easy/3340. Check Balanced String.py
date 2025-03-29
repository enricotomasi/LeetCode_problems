class Solution:
    def isBalanced(self, num: str) -> bool:
        one = 0
        two = 0
        flag = True

        for it in num:
            if flag:
                one += ord(it) - ord('0')
            else:
                two += ord(it) - ord('0')
            flag = not flag

        return one == two
        