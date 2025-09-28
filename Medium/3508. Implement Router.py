class Router:

    def __init__(self, memoryLimit: int):
        self.m = defaultdict(list)
        self.vis = set()
        self.q = deque()
        self.l = memoryLimit
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.vis:
            return False

        if len(self.q) == self.l:
            temp = self.q.popleft()
            self.m[temp[1]].pop(0)
            self.vis.remove(temp)

        self.m[destination].append(timestamp)
        self.vis.add((source, destination, timestamp))
        self.q.append((source, destination, timestamp))

        return True
        
    def forwardPacket(self) -> List[int]:
        if len(self.q) == 0:
            return []
        
        temp = self.q.popleft()

        source = temp[0]
        dest = temp[1]
        time = temp[2]

        self.vis.remove(temp)
        self.m[dest].pop(0)
        return [source, dest, time]
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        temp = self.m[destination]                  

        left = bisect.bisect_left(temp, startTime)
        right = bisect.bisect_right(temp, endTime)

        return right - left
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)