class Solution:
    def countTime(self, time: str) -> int:     
        
        ans = 1
        
        if time[3] == '?' and time[4] == '?':
            ans = 60
        elif time[3] == '?':
            ans = 6
        elif time[4] == '?':
            ans = 10

        if time[0] == '?' and time[1] == '?':
            ans *= 24
        elif time[0] == '?':
            m2 = ord(time[1]) - ord('0')
            if m2 < 4:
                ans *= 3
            else:
                ans *= 2
        elif time[1] == '?':
            m1 = ord(time[0]) - ord('0')
            if m1 < 2:
                ans *= 10
            else:
                ans *= 4

        return ans