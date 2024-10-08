class Solution
{
public:
    vector<vector<int>> transpose(vector<vector<int>> &matrix)
    {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<vector<int>> ans(n, vector<int>(m, 0));

        int r = 0;
        int c = 0;
        
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                ans[r][c] = matrix[i][j];

                r++;

                if (r >= n)
                {
                    r = 0;
                    c++;
                }
            }
        }

        return ans;
    }
};