class Solution
{
public:
    bool hasGroupsSizeX(vector<int> &deck)
    {
        unordered_map<int, int> m;

        for (auto it : deck)
        {
            m[it]++;
        }

        int temp = 0;

        for (auto it : m)
        {
            temp = __gcd(it.second, temp);
        }

        return temp >= 2;

    }
};
