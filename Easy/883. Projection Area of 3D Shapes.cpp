class Solution
{
public:
    int projectionArea(vector<vector<int>> &grid)
    {
        int n = grid.size();
        int ans = 0;

        for (int i = 0; i < n; ++i)
        {
            int a = 0;
            int b = 0;

            for (int j = 0; j < n; ++j)
            {
                a = max(a, grid[i][j]);
                b = max(b, grid[j][i]);
                
                if (grid[i][j] != 0)
                {
                    ans++;
                }

            }

            ans += a;
            ans += b;
        }

        return ans;
    }
};
