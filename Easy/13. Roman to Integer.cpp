class Solution 
{
public:
    int romanToInt(string s) 
    {
        int n = s.length();

        char last = '*';
        int ans = 0;

        for (int i = n - 1; i >= 0; i--)
        {
            char c = s[i];

            if (c == 'M')
            {
                ans += 1000;
                last = 'M';
            }
            else if (c == 'D')
            {
                ans += 500;
                last = 'D';
            }
            else if (c == 'C')
            {
                if (last == 'D' || last == 'M')
                {
                    ans -=100;
                }
                else
                {
                    ans += 100;
                    last = 'C';
                }
            }
            else if (c == 'L')
            {
                ans += 50;
                last = 'L';
            }
            else if (c == 'X')
            {
                if (last == 'L' || last == 'C')
                {
                    ans -= 10;
                }
                else
                {
                    ans += 10;
                    last = 'X';
                }
            }
            else if (c == 'V')
            {
                ans += 5;
                last = 'V';
            }
            else if (c == 'I')
            {
                if (last == 'V' || last == 'X')
                {
                    ans -= 1;
                }
                else
                {
                    ans += 1;
                    last = 'I';
                }
            }

        }

        return ans;

    }
};