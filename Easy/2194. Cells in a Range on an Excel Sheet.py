class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1 = ord(s[0]) - ord('A')
        r1 = ord(s[1]) - ord('0')

        c2 = ord(s[3]) - ord('A')
        r2 = ord(s[4]) - ord('0')

        # print(f"{c1} {r1}  ---  {c2} {r2}")

        ans = []

        for i in range(c1, c2 + 1):
            for j in range(r1, r2 + 1):
                ans += [ chr(i + ord('A')) + chr(j + ord('0')) ]

        return ans

        