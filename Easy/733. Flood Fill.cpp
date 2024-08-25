class Solution
{
public:
    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color)
    {
        int m = image.size();
        int n = image[0].size();
        vector<vector<bool>> vis(m, vector<bool>(n, false));
        
        int c = image[sr][sc];

        queue<pair<int, int>> q;
        q.push({sr, sc});

        while (!q.empty())
        {
            int x = q.front().first;
            int y = q.front().second;
            q.pop();
            
            // cout << x << ", " << y << endl;
            
            if (vis[x][y])
            {
                continue;
            }
            
            vis[x][y] = true;

            image[x][y] = color;

            if (x <  m  - 1 && image[x + 1][y] == c) q.push({x + 1, y});
            if (y <  n - 1 && image[x][y + 1] == c) q.push({x, y + 1});
            if (x > 0 && image[x - 1][y] == c) q.push({x - 1, y});
            if (y > 0 && image[x][y - 1] == c) q.push({x, y - 1});            
        }

        return image;

    }
};