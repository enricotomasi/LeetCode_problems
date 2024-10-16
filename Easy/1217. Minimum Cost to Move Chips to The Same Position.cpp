class Solution
{
public:
    int minCostToMoveChips(vector<int> &position)
    {
        int n = position.size();

        unordered_map<int, int> m;

        for (auto it : position)
        {
            m[it]++;
        }

        int odd = 0;
        int even = 0;
        

        for (auto it : m)
        {
            if (it.first % 2 == 0)
            {
                even += it.second;
            }
            else
            {
                odd += it.second;
            }
        }

        // cout << "odd: " << odd << " even: " << even << endl;

        return min(odd, even);
    }
};
