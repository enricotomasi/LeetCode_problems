class Solution
{
public:
    vector<vector<int>> imageSmoother(vector<vector<int>> &img)
    {
        int m = img.size();
        int n = img[0].size();

        vector<vector<int>> ans(m, vector<int>(n, 0));
        //                                7         8        9        6       3       2       1        4
        vector<vector<int>> moves = { {-1, -1}, {-1, 0}, {-1 , 1}, {0, 1}, {1, 1}, {1, 0}, {1, - 1}, {0, -1} };

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cout << endl << i << ", " << j << endl;

                int ns = 1;
                int sum = img[i][j];

                for (auto it : moves)
                {
                    int x = i + it[0];
                    int y = j + it[1];

                    if (x >= 0 && y >= 0 && x < m && y < n)
                    {
                        ns++;
                        sum += img[x][y];
                    }
                }

                ans[i][j] = sum / ns;

            }
        }

        return ans;
    }
};