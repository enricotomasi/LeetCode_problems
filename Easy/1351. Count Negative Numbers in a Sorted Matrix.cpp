class Solution
{
public:
    int countNegatives(vector<vector<int>> &grid)
    {
        int m = grid.size();
        int n = grid[0].size();

        int ans = 0;

        for (int i = m - 1; i >= 0; i--)
        {
            if (grid[i][n - 1] >= 0) break;
            for (int j = n - 1; j >= 0; j--)
            {
                if (grid[i][j] >= 0) break;
                ans++;
            }
        }

        return ans;
    }
};