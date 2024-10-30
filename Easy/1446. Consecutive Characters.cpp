class Solution
{
public:
    int maxPower(string s)
    {
        int n = s.length();

        int ans = 0;
        int temp = 1;

        for (int i = 1; i < n; i++)
        {
            if (s[i - 1] != s[i])
            {
                ans = max(ans, temp);
                temp = 1;
            }
            else
            {
                temp++;
            }
            
        }

        return max(ans, temp);
    }
};
