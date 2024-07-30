class Solution
{
public:
    int firstUniqChar(string s)
    {
        int n = s.length();
        int m[256] = { };

        for (char c : s)
        {
            m[c]++;
        }

        bool one = false;
        for (int i = 0; i < 256; i++)
        {
            if (m[i] == 1)
            {
                one = true;
                break;
            }
        }

        if (!one)
        {
            return -1;
        }

        for (int i = 0; i < n; i++)
        {
            if (m[s[i]] == 1)
            {
                return i;
            }
        }

        return -1;
    }
};