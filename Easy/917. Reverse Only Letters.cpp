class Solution
{
public:
    string reverseOnlyLetters(string s)
    {
        stack<char> v;
        for (char c : s)
        {
            if (tolower(c) >= 'a' && tolower(c) <= 'z' )
            {
                v.push(c);
            }
        }

        string ans = "";

        for (char c : s)
        {
            if (tolower(c) < 'a' || tolower(c) > 'z')
            {
                ans += c;
            }
            else
            {
                ans += v.top();
                v.pop();
            }
        }

        return ans;
    }
};
