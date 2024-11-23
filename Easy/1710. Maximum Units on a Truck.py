class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        n = truckSize

        box = sorted(boxTypes, key = lambda x : x[1], reverse = True)

        for i in range(len(box)):
            if n >= box[i][0]:
                n -= box[i][0]
                ans += box[i][0] * box[i][1]
            else:
                ans += box[i][1] * n
                return ans
        
        return ans
        