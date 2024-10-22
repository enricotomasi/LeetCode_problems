class Solution
{
public:
    int findSpecialInteger(vector<int> &arr)
    {
        unordered_map<int, int> m;

        for (auto it : arr)
        {
            m[it]++;
        }

        vector<pair<int, int>> v;

        for (auto it : m)
        {
            v.push_back({it.second, it.first});
        }

        sort(v.begin(), v.end());

        return v[v.size() - 1].second;
    }
};
