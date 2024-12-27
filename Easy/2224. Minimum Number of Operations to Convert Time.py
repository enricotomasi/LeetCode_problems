class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ms = int(current[0:2]) * 60
        ms += int(current[3:])

        # print(ms)

        mc = int(correct[0:2]) * 60
        mc += int(correct[3:])

        # print(mc)

        diff = mc - ms

        ans = 0

        while diff > 0:
            ans += 1
            if diff >= 60:
                diff -= 60
            elif diff >= 15:
                diff -= 15
            elif diff >= 5:
                diff -= 5
            else:
                diff -= 1
        
        return ans
