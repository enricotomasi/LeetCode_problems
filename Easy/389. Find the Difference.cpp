class Solution
{
public:
    char findTheDifference(string s, string t)
    {
        int mt[256] = { };

        for (char c : t)
        {
            mt[c]++;
        }

        int ms[256] = { };
        for (char c : s)
        {
            ms[c]++;
        }

        for (int i = 0; i < 256; i++)
        {
            if (mt[i] != ms[i])
            {
                return i;
            }
        }

        return '#';

    }
};