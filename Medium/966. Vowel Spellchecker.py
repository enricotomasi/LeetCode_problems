class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devov(s):
            ans = ""
            for c in s:
                if c.lower() in "aeiou":
                    ans += "_"
                else:
                    ans += c
            return ans

        s = set(wordlist)
        ins = {}
        d = {}

        for it in wordlist:
            dev = devov(it.lower())
            if it.lower() not in ins:
                ins[it.lower()] = it
            if dev not in d:
                d[dev] = it

        ans = []

        for it in queries:
            lower = it.lower()
            dev = devov(lower)

            add = ""
            
            if it in s:
                add = it
            elif lower in ins:
                add = ins[lower]
            elif dev in d:
                add = d[dev]
            
            ans += [add]

        return ans