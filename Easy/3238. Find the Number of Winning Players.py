class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        dic = { }

        for it in pick:
            key = str(it[0]) + '#' + str(it[1])
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1

        dic2 = { }

        for it in dic:
            p = ""
            for c in it:
                if c == '#':
                    break
                p += c
            
            player = int(p)

            if player in dic2:
                dic2[player] = max(dic2[player] , dic[it])
            else:
                dic2[player] = dic[it]
        
        ans = 0

        for it in dic2:
            if it < dic2[it]:
                ans += 1

        return ans
                
            

 