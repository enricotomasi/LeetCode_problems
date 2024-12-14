class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        last = 'a'
        
        for c in word:
            if c == last:
                ans += 1
                continue

            cn = ord(c) - ord('a')
            ln = ord(last) - ord('a')

            forw = 1
            rev = 1
            
            if cn > ln:
                forw += cn - ln
                rev += 25 - cn + ln + 1
            else:
                forw += ln - cn
                rev += cn + 25 - ln + 1
            
            ans += min(forw, rev)
            last = c
            
            # print(f"c: {c} last: {last} cn: {cn} ln: {ln}  forw: {forw} rev: {rev}  *** min: {min(forw, rev)}  ans: {ans}")
        
        return ans
