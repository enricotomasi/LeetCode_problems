def convert(s):
    doms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = int(s[0 : 2])
    ans = int(s[3: 5])
    
    for i in range(month - 1):
        ans += doms[i]
    
    return ans
    

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        aa = convert(arriveAlice)
        la = convert(leaveAlice)

        ab = convert(arriveBob)
        lb = convert(leaveBob)

        ans = min(la, lb) - max(aa, ab) + 1

        if ans < 0:
            return 0

        return ans