class Solution:
    def reformatDate(self, date: str) -> str:
        year = ""
        month = ""
        day = ""

        months = {"Jan" : "1", "Feb" : "2", "Mar" : "3", "Apr" : "4", "May": "5", "Jun" : "6", "Jul" : "7", "Aug" : "8", "Sep" : "9", "Oct" : "10", "Nov" : "11", "Dec" : "12"}

        n = len(date)
        i = 0

        # Step 1 day
        while date[i].isdigit():
            day += date[i]
            i += 1

        # Step 2 day suffix
        while date[i] != " ":
            i += 1

        # Step 3 month
        i += 1
        while date[i] != " ":
            month += date[i]
            i += 1
        
        # Step 4 year
        i += 1
        while i < n:
            year += date[i]
            i += 1
        
        if len(day) < 2:
            day = "0" + day
        
        month = months[month]
        
        if len(month) < 2:
            month = "0" + month
        
        return year + "-" + month + "-" + day
        