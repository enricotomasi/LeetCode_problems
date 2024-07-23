class Solution
{
public:
    static bool cmp(pair<int, int> &a, pair<int, int> &b)
    {
        if (a.second == b.second)
        {
            return a.first > b.first;
        }
        
        return a.second < b.second;
    }
    
    
    vector<int> frequencySort(vector<int> &nums)
    {
        map<int, int> m;

        for (auto it : nums)
        {
            m[it]++;
        }

        vector<pair<int, int>> v;
        for (auto it : m)
        {
            v.push_back({ it.first, it.second });
        }

        sort(v.begin(), v.end(), cmp);

        vector<int> ans;

        for (auto it : v)
        {
            for (int i = 0; i < it.second; i++)
            {
                ans.push_back(it.first);
            }
        }

        return ans;
    }
};