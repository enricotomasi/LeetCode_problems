class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]

        for it in edges:
            g[it[0]].append(it[1])
            g[it[1]].append(it[0])

        q = deque([source])
        vis = [0] * n
        vis[source] = 1

        while q:
            current = q.popleft()
            if current == destination:
                return True 

            for it in g[current]:
                if vis[it] == 0:
                    vis[it] = 1
                    q.append(it)
        
        return False
