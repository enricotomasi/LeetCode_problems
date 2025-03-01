class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n = len(capacity)

        totapp = 0
        for it in apple:
            totapp += it

        capacity.sort(reverse = True)
        
        for i in range(n):
            totapp -= capacity[i]
            if totapp <= 0:
                return i + 1
        
        return -1
