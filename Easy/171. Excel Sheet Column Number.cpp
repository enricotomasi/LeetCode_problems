class Solution
{
public:
    int titleToNumber(string columnTitle)
    {
        string s = columnTitle;
        int n = s.length();
        cout << "s: " << s << " n: " << n << endl;

        int ans = s[n - 1] - 'A' + 1;

        // cout << "s[n - 1]  - 'A' + 1: " << ans << endl;

        int mul = 1;
        for (int i = n - 2; i >= 0; i--)
        {
            int temp = (s[i] - 'A' + 1) * pow(26, mul);
            ans += temp;

            mul++;
            // cout << "char: " << s[i] << " temp: " << temp << " ans: " << ans << endl;

        }

        return ans;

    }
};