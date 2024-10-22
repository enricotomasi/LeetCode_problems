class Solution
{
public:
    string tictactoe(vector<vector<int>> &moves)
    {
        int n = moves.size();
        vector<vector<int>> grid(3, vector<int>(3, 0));

        bool one = true;

        for (auto it : moves)
        {
            if (one)
            {
                grid[it[0]][it[1]] = 1;
            }
            else //two
            {
                grid[it[0]][it[1]] = 2;
            }
           one = !one;
        }

        for (int i = 0; i < 3; i++)
        {
            string win = "";
            
            if (grid[i][0] == 1 && grid[i][1] == 1 && grid[i][2] == 1) return "A";
            if (grid[i][0] == 2 && grid[i][1] == 2 && grid[i][2] == 2) return "B";

            if (grid[0][i] == 1 && grid[1][i] == 1 && grid[2][i] == 1) return "A";
            if (grid[0][i] == 2 && grid[1][i] == 2 && grid[2][i] == 2) return "B";
        }

        if (grid[0][0] == 1 && grid[1][1] == 1 && grid[2][2] == 1) return "A";
        if (grid[0][0] == 2 && grid[1][1] == 2 && grid[2][2] == 2) return "B";

        if (grid[0][2] == 1 && grid[1][1] == 1 && grid[2][0] == 1) return "A";
        if (grid[0][2] == 2 && grid[1][1] == 2 && grid[2][0] == 2) return "B";
        
        if (n == 9) return "Draw";
        return "Pending";

    }
};
