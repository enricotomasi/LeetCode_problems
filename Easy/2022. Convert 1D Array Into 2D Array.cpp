class Solution
{
public:
    vector<vector<int>> construct2DArray(vector<int> &original, int m, int n)
    {
        int no = original.size();

        if (no != m * n)
        {
            // cout << "different" << endl;
            return { };
        }

        if (m == 1)
        {
            // cout << "one row" << endl;
            vector<vector<int>> ans;
            ans.push_back(original);
            return ans;
        }
        
        vector<vector<int>> ans(m, vector<int>(n, 0));

        // cout << "m: " << ans.size() << " n: " << ans[0].size() << " no: " << no << endl;

        int j = 0; 
        int k = 0;

        for (int i = 0; i < no; i++)
        {
            // cout << i << "# " << " original[i]: " << original[i] << "  ---- j: " << j << " k: " << k << endl;

            ans[j][k] = original[i];
            
            k++;

            if (k >= n)
            {
                k = 0;
                j++;
            }

        }     

        return ans;
    }
};