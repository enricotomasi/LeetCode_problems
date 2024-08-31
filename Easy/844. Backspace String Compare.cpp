class Solution
{
public:
    string clean(string s)
    {
        // cout << s << " ";
        int n = s.length();
        string ans = "";
        
        for (int i = 0; i < n; i++)
        {
            if (s[i] == '#')
            {
                if (ans.length() > 1)
                {
                    ans = ans.substr(0, ans.length() - 1);
                }
                else if (ans.length() == 1)
                {
                    ans = "";
                }
            }
            else
            {
                ans += s[i];
            }
        }
        
        // cout << ans << endl;
        return ans;
    }
    
    bool backspaceCompare(string s, string t)
    {
        return clean(s) == clean(t);
    }
};