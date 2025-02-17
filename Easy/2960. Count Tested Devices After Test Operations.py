class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        ans = 0

        for i in range(n):
            if batteryPercentages[i] > 0:
                ans += 1
                for j in range(i + 1, n):
                    if batteryPercentages[j] > 0:
                        batteryPercentages[j] -= 1
            
        
        return ans    
