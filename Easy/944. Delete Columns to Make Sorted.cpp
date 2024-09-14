class Solution
{
public:
    int minDeletionSize(vector<string> &strs)
    {
        int ans = 0;
        int rows = strs.size();
        int cols = strs[0].size();

        for (int col = 0; col < cols; col++)
        {
            bool ok = true;
            
            for (int row = 0; row < rows - 1; row++)
            {
                if (strs[row][col] > strs[row + 1][col])
                {
                    ok = false;
                    break;
                }
            }

            if (!ok)
            {
                ans++; 
            }
        }

        return ans;
    }
};
