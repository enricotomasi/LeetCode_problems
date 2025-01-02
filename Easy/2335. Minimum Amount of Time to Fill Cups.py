class Solution:
    def fillCups(self, amount: List[int]) -> int:
        am2 = []

        for it in amount:
            if it > 0:
                am2 += [it]

        if len(am2) == 0:
            return 0

        ans = 0

        while (len(am2) > 0 and am2[0] > 0) or len(am2) > 1:
            am2.sort(reverse = True)            
            ans += 1

            if len(am2) == 1:
                am2[0] -= 1
                if am2[0] <= 0:
                    am2 = am2[ 1 : ]
            else:
                am2[0] -= 1
                am2[1] -= 1

                if am2[1] <= 0:
                    am2 = [am2[0]] + am2[ 2 : ]
        
        return ans
