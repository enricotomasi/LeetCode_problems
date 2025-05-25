class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        double = 0
        dic = {}
        double = {}

        for s in words:
            if s[0] == s[1]:
                if s in double:
                    double[s] += 1
                else:
                    double[s] = 1
            else:
                if s in dic:
                    dic[s] += 1
                else:
                    dic[s] = 1
            
        # print(dic)
        # print(double)
        
        ans = 0

        # print(f"\nsingles:")
        for s in words:
            r = s[1] + s[0]
            # print(f"    -> string: {s} reverse: {r}")
            if s == r:
                # print(f"        -> double, continue")
                continue
            if r in dic and dic[r] > 0 and dic[s] > 0:
                ans += 4
                dic[s] -= 1
                dic[r] -= 1
                # print(f"        -> reverse found ans: {ans}  dic[s]: {dic[s]}, dic[r]: {dic[r]}")

        # print(f"\n doubles:")
        jolly = False
        for it in double:
            # print(f"    -> {it}")
            if double[it] >= 2:
                ans += 4 * (double[it] // 2)
                #double[it] -= double[it] // 2 # debug
                # print(f"        -> double[it] > 2, double[it] // 2 = {double[it] % 2 > 0} ans = {ans}")
                if double[it] % 2 > 0:
                    # print(f"        -> reminder, set jolly true")
                    jolly = True
            elif double[it] > 0:
                # print(f"        -> double[it] > 0, set jolly true")
                jolly = True

        # print("\n")
        # print(dic)
        # print(double)

        if jolly:
            ans += 2
            # print(f"\njolly, new ans: {ans}")

        
        return ans