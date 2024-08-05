class Solution
{
public:
    int islandPerimeter(vector<vector<int>> &grid)
    {
        int rows = grid.size();

        if (rows == 0)
        {
            return 0;
        }

        int cols = grid[0].size();

        cout << "rows: " << rows << endl << "cols: " << cols << endl;

        int ans = 0;

        for (int x = 0; x < rows; x++)
        {
            for (int y = 0; y < cols; y++)
            {
                if (grid[x][y] == 1)
                {
                    if (x - 1 < 0 || grid[x - 1][y] == 0) ans++;
                    if (y - 1 < 0 || grid[x][y - 1] == 0) ans++;
                    if (x + 1 >= rows || grid[x + 1][y] == 0) ans++;
                    if (y + 1 >= cols || grid[x][y + 1] == 0) ans++;
                }
            }
        }

        return ans;
    }
};