class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ans = 0
        d = dict()

        for i in range(1950, 2051):
            d[i] = 0

        for it in logs:
            for i in range(it[0], it[1]):
                d[i] += 1

        ans = 2090
        m = -1

        for it in d:
            # print(f"{it} - {d[it]}")
            if d[it] > m or (d[it] == m and ans > it):
                ans = it
                m = d[it]

        return ans
