class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        temp = 0

        while (mainTank > 0):
            ans += 10
            mainTank -= 1
            temp += 1

            if temp == 5 and additionalTank > 0:
                temp = 0
                additionalTank -= 1
                mainTank += 1
        
        return ans