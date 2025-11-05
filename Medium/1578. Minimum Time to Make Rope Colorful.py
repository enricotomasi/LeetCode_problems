class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)

        last = 'z'
        temp = []
        groups = []

        for i in range(n):
            if colors[i] == last:
                temp.append(neededTime[i])
            else:
                groups.append(temp)
                temp = [neededTime[i]]
                last = colors[i]
        
        if len(temp) > 0:
            groups.append(temp)

        ans = 0

        for it in groups:
            if len(it) <= 1:
                continue
            
            it.sort()
        
            for i in range(len(it) - 1):
                ans += it[i]
            
        return ans