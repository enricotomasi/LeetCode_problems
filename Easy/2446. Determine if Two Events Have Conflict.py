class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        time1start = (int(event1[0][ : 2]) * 60) + int(event1[0][3 : ])
        time1end = (int(event1[1][ : 2]) * 60) + int(event1[1][3 : ])

        # print(time1start, time1end)

        time2start = (int(event2[0][ : 2]) * 60) + int(event2[0][3 : ])
        time2end = (int(event2[1][ : 2]) * 60) + int(event2[1][3 : ])

        # print(time2start, time2end)

        if (time1start <= time2end and time1start >= time2start) or (time1end <= time2end and time1end >= time2start) or (time2start <= time1end and time2start >= time1start) or (time2end <= time1end and time2end >= time1start):
            return True
        
        return False
