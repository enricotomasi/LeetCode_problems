class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        arr = []

        for it in grid:
            it.sort(reverse = True)
            arr += [it]

        rows = len(arr) 
        cols = len(arr[0])

        ans = 0
        
        for i in range(cols):
            toadd = -1
            
            for j in range(rows):
                toadd = max(toadd, arr[j][i])

            ans += toadd
            

        return ans        
