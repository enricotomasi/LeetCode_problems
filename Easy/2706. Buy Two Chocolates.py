class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = 101
        min2 = 101

        for it in prices:
            if it < min1 and it < min2:
                if min1 > min2:
                    min1, min2 = min2, min1
                min2 = it
            elif it < min1:
                min1 = it
            elif it < min2:
                min2 = it
            
            # print(it, " ", min1, min2)
            

        # print(min1, min2)           
        
        if min1 == 101 or min2 == 101 or min1 + min2 > money:
            return money

        return money - min1 - min2