class Solution
{
public:
    static bool cmp(pair<int, string> &a, pair<int, string> &b)
    {
        return a.first > b.first;
    }

    vector<string> sortPeople(vector<string> &names, vector<int> &heights)
    {
        int n = names.size();

        vector<pair<int, string>> m;

        for (int i = 0; i < n; i++)
        {
            m.push_back({ heights[i], names[i] });
        }

        sort(m.begin(), m.end(), cmp);

        vector<string> ans;

        for (auto it : m)
        {
            ans.push_back(it.second);
        }

        return ans;
    }
};