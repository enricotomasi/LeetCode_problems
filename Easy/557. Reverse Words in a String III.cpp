class Solution
{
public:
    string reverseWords(string s)
    {
        if (s == "")
        {
            return s;
        }

        string ans = "";

        string temp = "";

        for (char c : s)
        {
            if (c == ' ' && temp != "")
            {
                reverse(temp.begin(), temp.end());
                ans += temp + ' ';
                temp = "";
            }
            else
            {
                temp += c;
            }
        }

        reverse(temp.begin(), temp.end());
        ans += temp;

        return ans;


    }
};