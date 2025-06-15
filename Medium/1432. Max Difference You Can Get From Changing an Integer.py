class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        sub = '0'

        for c in s:
            if c != '9':
                sub = c
                break

        first = int(s.replace(sub, '9'))

        rep = '1'
        dig = s[0]
        sub = dig

        if dig == '1':
            for i in s:
                if i != '0' and i != dig:
                    sub = i
                    rep = '0'
                    break

        second = int(s.replace(sub, rep))

        return first - second