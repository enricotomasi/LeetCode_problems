class Solution:
    def minLength(self, s: str) -> int:
        # print(s)
        mods = 69

        while mods != 0 and len(s) > 0:
            mods = 0
            ns = ""
            n = len(s)
            i = 0
            
            while (i < n):
                if i == n - 1 or (not (s[i] == 'A' and s[i + 1] == 'B') and not (s[i] == 'C' and s[i + 1] == 'D')):
                    ns += s[i]
                    i += 1
                else:
                    mods += 1
                    i += 2

            s = ns
            # print(s)

        return len(s)
