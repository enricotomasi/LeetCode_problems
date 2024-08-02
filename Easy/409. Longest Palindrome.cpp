class Solution
{
public:
    int longestPalindrome(string s)
    {
        int n = s.length();

        cout << "n: " << n << endl;

        int m[256] = { };

        for (char c : s)
        {
            m[c]++;
        }

        int ans = 0;

        for (int i = 0; i < 256; i++)
        {
            if (m[i] != 0) cout << (char)i << " " << m[i] << endl;
            ans += (m[i] / 2) * 2;
        }

        if (ans != n)
        {
            ans++;
        }

        return ans;
    }
};