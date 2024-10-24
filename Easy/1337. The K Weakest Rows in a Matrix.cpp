class Solution
{
public:
    static bool cmp(pair<int, int> &a, pair<int, int> &b)
    {
        if (a.second == b.second)
        {
            return a.first < b.first;
        }

        return a.second < b.second;
    }
    
    vector<int> kWeakestRows(vector<vector<int>> &mat, int k)
    {
        int m = mat.size();
        int n = mat[0].size();

        vector<pair<int, int>> v;

        for (int i = 0; i < m; i++)
        {
            int temp = 0;
            for (int j = 0; j < n; j++)
            {
                if (mat[i][j] == 1)
                {
                    temp++;
                }
            }
            v.push_back({i, temp});
        }

        sort(v.begin(), v.end(), cmp);

        // for (auto it : v) cout << it.first << ", " << it.second << endl;

        vector<int> ans;

        int count = 0;
        for (int i = 0; i < v.size(); i++)
        {
            if (count >= k) break;
            ans.push_back(v[i].first);
            count++;
        }

        return ans;

    }
};