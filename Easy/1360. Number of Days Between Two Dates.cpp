class Solution
{
public:
    bool leap(int year)
    {
        bool ans = false;

        if (year % 4 == 0)
        {
            ans = true;
        }
        
        if (year % 100 == 0)
        {
            ans = false;
        }
        
        if (year % 400 == 0)
        {
            ans = true;
        }
        
        return ans;
    }
    
    int daysBetweenDates(string date1, string date2)
    {
        int y1 = stoi(date1.substr(0, 4));
        int m1 = stoi(date1.substr(5,2));
        int d1 = stoi(date1.substr(8, 2));
        
        int y2 = stoi(date2.substr(0, 4));
        int m2 = stoi(date2.substr(5,2));
        int d2 = stoi(date2.substr(8, 2));

        if (y1 > y2 || (y1 == y2 && m1 > m2) || (y1 == y2 && m1 == m2 && d1 > d2))
        {
            int ty1 = y1;
            int tm1 = m1;
            int td1 = d1;

            y1 = y2;
            m1 = m2;
            d1 = d2;

            y2 = ty1;
            m2 = tm1;
            d2 = td1;
        }
        
        // cout << y1 << " " << m1 << " " << d1 << endl;
        // cout << y2 << " " << m2 << " " << d2 << endl;
        
        if (y1 == y2 && m1 == m2)
        {
            // cout << "same year and same month" << endl;
            return d2 - d1;
        }

        vector<int> m = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        if (leap(y1))
        {
            m[1] = 29;
            // cout << "leap year1: " << y1 << endl;
        } 
        int ans = 0;

        if (y1 == y2)
        {
            // cout << "same year" << endl;

            ans = m[m1 - 1] - d1;
            // cout << endl << "after d1: " << ans << endl;
            
            for (int i = m1; i < m2 - 1; i++)
            {
                ans += m[i];
                // cout << "m: " << i << " ans: " << ans << endl;
            }

            // cout << endl << "after m : " << ans << endl;
            
            ans += d2;

            // cout << endl << "after d2: " << ans << endl;
            return ans;
        }
        
        // cout << endl << "not same year" << endl;
      
        ans = m[m1 - 1] - d1;
        // cout << endl << "after d1: " << ans << endl;

        for (int i = m1; i < 12; i++)
        {
            ans += m[i];
            // cout << "m: " << i << " ans: " << ans << endl;
        }

        // cout << endl << "after m1: " << ans << endl;

        for (int i = y1 + 1; i < y2; i++)
        {
            if (leap(i)) ans += 366;
            else ans += 365;
            // cout << "year: " << i << " leap: " << leap(i) << " ans: " << ans << endl;
        }

        // cout << endl << "after y : " << ans << endl;

        if (leap(y2))
        {
            m[1] = 29;
            // cout << "leap year2: " << y2 << endl;
        } 
        else
        {
            m[1] = 28;
        } 
        
        for (int i = 0; i < m2 - 1; i++)
        {
            ans += m[i];
            // cout << "m: " << i << " ans: " << ans << endl;
        }

        // cout << endl << "after m2: " << ans << endl;

        ans += d2;

        // cout << endl << "after d2: " << ans << endl;

        return ans;
    }
};
