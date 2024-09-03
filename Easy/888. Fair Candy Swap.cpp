class Solution
{
public:
    vector<int> fairCandySwap(vector<int> &aliceSizes, vector<int> &bobSizes)
    {
        int na = 0;
        for (auto it : aliceSizes)
        {
            na += it;
        }

        int nb = 0;
        for (auto it : bobSizes)
        {
            nb += it;
        }

        cout << "na: " << na << " nb: " << nb << endl;

        for (auto it : aliceSizes)
        {
            for (auto it2: bobSizes)
            {
                if ((na - it + it2) == (nb - it2 + it))
                {
                    return {it, it2};
                }
            }

        }

        return {-1, -1};
    }
};
