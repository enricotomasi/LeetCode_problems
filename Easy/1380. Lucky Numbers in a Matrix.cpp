class Solution
{
public:
    vector<int> luckyNumbers (vector<vector<int>> &matrix)
    {
        int m = matrix.size();

        if (m == 0)
        {
            return { };
        }

        int n = matrix[0].size();

        // cout << "m: " << m << " n: " << n << endl;

        unordered_set<int> mr;

        for (int i = 0; i < m; i ++)
        {
            int temp = INT_MAX;
            for (int j = 0; j < n; j++)
            {
                temp = min(temp, matrix[i][j]);
            }
            mr.insert(temp);
        }

        // cout << "min row: ";
        // for (auto it : mr) cout << it << " ";
        // cout << endl;

        vector<int> ans;

        for (int j = 0; j < n; j++)
        {
            int temp = INT_MIN;
            for (int i = 0; i < m; i++)
            {
                // cout << "matrix[" << i << "][" << j << "]: "<< matrix[i][j] << endl;
                temp = max(temp, matrix[i][j]);
            }

            // cout << "temp: " << temp << endl;
            if (mr.find(temp) != mr.end())
            {
                // cout << "Bingo!" << endl;
                ans.push_back(temp);
            }

        }

        return ans;
    }
};