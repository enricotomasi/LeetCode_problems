class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = { }

        for it in items1:
            if it[0] in d:
                d[it[0]] += it[1]
            else:
                d[it[0]] = it[1]
        
        for it in items2:
            if it[0] in d:
                d[it[0]] += it[1]
            else:
                d[it[0]] = it[1]

        d = dict(sorted(d.items()))

        ans = []

        for it in d:
            ans += [[it, d[it]]]
        
        return ans
        