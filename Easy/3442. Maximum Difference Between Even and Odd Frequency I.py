class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0 for _ in range(26)]

        for c in s:
            freq[ord(c) - ord('a')] += 1
        
        odd = set()
        even = set()

        for i in range(26):
            if freq[i] > 0:
                if freq[i] % 2 == 0:
                    even.add(freq[i])
                else:
                    odd.add(freq[i])

        o = list(odd)
        e = list(even)
        
        o.sort()
        e.sort()
        
        if len(o) < 1 or len(e) < 1:
            return -1

        return o[len(o) - 1] - e[0]