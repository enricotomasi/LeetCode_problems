class Solution
{
public:
    int getLucky(string s, int k)
    {
        string s1 = "";

        for (char c : s)
        {
            s1 += to_string((int)c - 'a' + 1);
        }

        // cout << s1 << endl;

        int ans = 0;
        for (int i = 0; i < k; i++)
        {
            ans = 0;

            for (char c : s1)
            {
                ans += c - '0';
            }

            s1 = to_string(ans);
        }


        return ans;
    }
};
