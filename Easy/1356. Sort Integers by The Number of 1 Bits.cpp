class Solution
{
public:
    static bool cmp(const int &a, const int &b)
    {
        int oa = 0;
        int ca = a;

        while (ca)
        {
            if (ca % 2 == 1) oa++;
            ca /= 2;
        }

        int ob = 0;
        int cb = b;

        while (cb)
        {
            if (cb %2 == 1) ob++;
            cb /= 2;
        }

        if (oa == ob)
        {
            return a < b;
        }

        return oa < ob;

    }

    vector<int> sortByBits(vector<int> &arr)
    {
        sort(arr.begin(), arr.end(), cmp);
        return arr;
    }
};