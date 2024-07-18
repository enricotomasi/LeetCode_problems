class Solution 
{
public:
    vector<vector<int>> generate(int numRows) 
    {
        vector<vector<int>> ans;

        if (numRows == 0)
        {
            return ans;
        }

        ans.push_back({1});

        if (numRows == 1)
        {
            return ans;
        }

        for (int i = 2; i <= numRows; i++)
        {
            vector<int> temp;
            temp.push_back(1);
            
            int nlast = ans.size();
            vector<int> last = ans[nlast - 1];

            for (int j = 1; j < i - 1; j++)
            {
                temp.push_back(last[j - 1] + last[j]);
            }

            temp.push_back(1);
            ans.push_back(temp);
        }


        return ans;
    }
};