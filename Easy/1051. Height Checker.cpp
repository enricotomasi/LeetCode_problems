class Solution
{
public:
    int heightChecker(vector<int> &heights)
    {
        int n = heights.size();
        
        vector<int> ord(heights);
        sort(ord.begin(), ord.end());

        int ans = 0;

        for (int i = 0; i < n; i++)
        {
            if (heights[i] != ord[i])
            {
                ans++;
            }
        }

        return ans;
    }
};
