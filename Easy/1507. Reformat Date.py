class Solution:
    def reformatDate(self, date: str) -> str:
        year = ""
        month = ""
        day = ""

        months = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May": "05", "Jun" : "06", "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}

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
               
        return year + "-" + month + "-" + day
        