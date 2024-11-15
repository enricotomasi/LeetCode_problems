class OrderedStream:
    ptr = 1
    arr = [[] for _ in range(1000)]

    def __init__(self, n: int):
        self.arr = ["" for _ in range(n)] * n
        self.ptr = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value

        ans = []

        if self.ptr == idKey - 1:
            n = len(self.arr)
            while self.ptr < n and self.arr[self.ptr] != "":
                ans.append(self.arr[self.ptr])
                self.ptr += 1

        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
