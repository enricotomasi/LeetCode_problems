class Solution
{
public:
    vector<vector<int>> allCellsDistOrder(int rows, int cols, int rCenter, int cCenter)
    {

        vector<pair<int, pair<int,int>>> temp;

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                temp.push_back({abs(i - rCenter) + abs(j - cCenter), {i, j}});
            }
        }

        sort(temp.begin(), temp.end());

        vector<vector<int>> ans;
        
        for (auto it : temp)
        {
            ans.push_back({it.second.first, it.second.second});
        }

        return ans;
    }
};