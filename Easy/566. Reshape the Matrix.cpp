class Solution
{
public:
    vector<vector<int>> matrixReshape(vector<vector<int>> &mat, int r, int c)
    {
        int m = mat.size();
        int n = mat[0].size();

        // cout << "n: " << n << " m: " << m << "  ---  r: " << r << " c: " << c << endl;
        // cout << "n * m: " << (n * m) << " r * c: " << (r * c) << endl;

        if ((n * m) != (r * c))
        {
            return mat;
        }

        vector<vector<int>> ans(r, vector<int> (c, 0));

        // cout << "ans size: " << ans.size() << " x " << ans[0].size() << endl << endl;

        int k = 0; // rows
        int l = 0; // cols

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                // cout << endl << "i: " << i << " j: " << j << " ---  k: " << k << " l: " << l << endl;
                
                // cout << mat[i][j];
                // cout << "  ---  " << ans[k][l];
                
                // cout << endl;

                ans[k][l] = mat[i][j];

                if (l < c - 1)
                {
                    l++;
                }
                else
                {
                    l = 0;
                    k++;
                }

            }
        }
        
        return ans;
    }
};