class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        paid = 0

        for it in brackets:
            if it[0] >= income:
                ans += (income - paid) * it[1] / 100
                return ans
            else:
                ans += (it[0] - paid) * it[1] / 100
                paid = it[0]
        
        return ans