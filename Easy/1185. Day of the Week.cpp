class Solution
{
public:
    bool leap (int year)
    {
        return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }
    
    string dayOfTheWeek(int day, int month, int year)
    {
        // 1971 01 01 = friday (5)

        int dist = 0;
        int y = 1971;
        
        while (y < year)
        {
            // cout << " year: " << y;
            if (leap(y))
            {
                // cout << " leap, add 366";
                dist += 366;
            }
            else
            {
                // cout << "       add 365";
                dist += 365;
            }
            // cout << " dist: " << dist << endl;
            y++;
        }

        // cout << endl;

        vector<string> dow = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        //               1   2   3   4   5   6   7   8   9   10  11  12 
        vector<int> m = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        if (leap(year))
        {
            m[1] = 29;
        }

        for (int i = 0; i < month - 1; i++)
        {
            // cout << "Month: " << i + 1 << " days: " << m[i] << " dist: " << dist << endl;
            dist += m[i];
        }

        
        // cout << "  day: " << day << " dist: " << dist << endl;
        
        dist += day;

        return dow[(dist + 4) % 7];
    }
};