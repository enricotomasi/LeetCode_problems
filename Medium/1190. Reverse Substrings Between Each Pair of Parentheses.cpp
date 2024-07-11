class Solution 
{
public:
    string reverseParentheses(string s)
    {
        
        bool par = true;

        while (par)
        {
            // cout << endl << "s: " << s << endl;
            par = false;

            int start = -1;
            int end = -1;

            for (int i = 0; i < s.length(); i++)
            {
                if (s[i] == '(')
                {
                    par = true;
                    start = i;
                }
                else if (s[i] == ')')
                {
                    string sub = s.substr(start + 1, i - start - 1);
                    // cout << "start: " << start << " i: " << i << " sub: " << sub << endl;
                    reverse(sub.begin(), sub.end());

                    string first = s.substr(0, start);
                    string last = s.substr(i + 1);
                    // cout << "***first: " << first << " ***sub: " << sub << " ***last: " << last << endl;
                    s = first + sub + last;
                
                    break;
                }
            }
        }

        return s;

    }
};