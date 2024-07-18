class Solution
{
public:
    bool isPalindrome(string s)
    {
        int n = s.length();
        string san = "";

        for (int i = 0; i < n; i++)
        {
            if (s[i] >= 'A' && s[i] <= 'Z')
            {
                san += s[i] + 32;
            }
            else if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= '0' && s[i] <= '9'))
            {
                san += s[i];
            }
        }

        string rev = san;
        reverse(rev.begin(), rev.end());

        return san == rev;

    }
};