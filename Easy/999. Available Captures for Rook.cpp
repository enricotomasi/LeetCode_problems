class Solution
{
public:
    int calc(vector<vector<char>> &board, int x, int y)
    {
        // cout << x << ", " << y << ": " << board[x][y] << endl;
        if (board[x][y] == 'p')
        {
            return 1;
        }
        else if (board[x][y] != '.')
        {
            return -1;
        }

        return 0;
    }
    
    int numRookCaptures(vector<vector<char>> &board)
    {
        int px;
        int py;

        for (px = 0; px < 8; px++)
        {
            bool ok = false;
            for (py = 0; py < 8; py++)
            {
                // cout << board[px][py] << " ";
                if (board[px][py] == 'R')
                {
                    ok = true;
                    break;
                }
            }
            // cout << endl;
            if (ok)
            {
                break;
            }
        }

        // cout << "rock: " << px << ", " << py << endl;

        int ans = 0;

        for (int i = px + 1; i < 8; i++)
        {
            int add = calc(board, i, py);
            if (add < 0) break;
            ans += add;
            if (add > 0) break;
        }

        for (int i = py + 1; i < 8; i++)
        {
            int add = calc(board, px, i);
            if (add < 0) break;
            ans += add;
            if (add > 0) break;
        }

        for (int i = px - 1; i >= 0; i--)
        {
            int add = calc(board, i, py);
            if (add < 0) break;
            ans += add;
            if (add > 0) break;
            
        }

        for (int i = py - 1; i >= 0; i--)
        {
            int add = calc(board, px, i);
            if (add < 0) break;
            ans += add;
            if (add > 0) break;
        }


        return ans;
    }
};