class Solution
{
public:
    int oddCells(int m, int n, vector<vector<int>> &indices)
    {
        vector<vector<bool>> v(m, vector<bool>(n, false));

        for (auto it : indices)
        {
            int r = it[0];
            for (int i = 0; i < n; i++)
            {
                v[r][i] = !v[r][i];
            }

            int c = it[1];
            for (int i = 0; i < m; i++)
            {
                v[i][c] = !v[i][c];
            }
        }

        int ans = 0;
        for (auto it : v)
        {
            for (auto it2 : it)
            {
                if (it2)
                {
                    ans++;
                }
            }
        }
        
        return ans;
    }
};