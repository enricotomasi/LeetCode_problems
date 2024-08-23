class Solution
{
public:
    int countBinarySubstrings(string s)
    {
        int n = s.length();
        
        if (n == 0)
        {
            return 0;
        }    

        int last = 0;
        int curr = 1;
        int ans = 0;

        for (int i = 1; i < n; i++)
        {
            if (s[i] == s[i - 1])
            {
                curr++;
            }
            else
            {
                last = curr;
                curr = 1;
            }
            if (last >= curr)
            {
                ans++;
            }
        }

        return ans;
    }
};