class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)

        s1 = s[ 0 : n // 2]

        start = n // 2
        if n % 2 != 0:
            start += 1
        
        s2 = s [ start : ]

        print(f"{s1} --- {s2}")

        a1 = ""
        a2 = ""

        nh = len(s1)
        
        for i in range(len(s1)):
            c = min(s1[i], s2[nh - i - 1])
            a1 += c
            a2 = c + a2

        if n % 2 != 0:
            a1 += s[(n // 2)]
        
        a1 += a2

        return a1