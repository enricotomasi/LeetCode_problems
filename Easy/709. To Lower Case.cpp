class Solution
{
public:
    string toLowerCase(string s)
    {
        string ans = "";

        for (char c : s)
        {
            if (c >= 'A' && c <= 'Z')
            {
                ans += c + 32 ;
            }
            else
            {
                ans += c;
            }
        }

        return ans;   
    }
};