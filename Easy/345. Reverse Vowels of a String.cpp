class Solution
{
public:
    string reverseVowels(string s)
    {
        string ans = "";
        stack<char> st;

        for (char c : s)
        {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
             || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            {
                st.push(c);
            }
        }

        for (char c : s)
        {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
             || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            {
                ans += st.top();
                st.pop();
            }
            else
            {
                ans += c;
            }
        }

        return ans;
    }
};