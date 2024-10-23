class Solution
{
public:
    string freqAlphabets(string s)
    {
        int n = s.length();
        string ans = "";

        for (int i = 0; i < n; i++)
        {
            if (s[i] != '#')
            {
                int c = s[i] + 48;
                // cout << s[i] << ": " << "c: " << c << " (char)c:" << (char)c << endl;
                ans += c;
            }
            else
            {
                ans = ans.substr(0, ans.size() - 2);
                
                string temp = "";
                temp += s[i - 2];
                temp += s[i - 1];

                int t = stoi(temp);
                // cout << "t: " << t << endl;
                int c = t + 96;
                ans += c;
            }
        }

        return ans;    
    }
};
