class Solution
{
public:
    vector<bool> kidsWithCandies(vector<int> &candies, int extraCandies)
    {
        int n = candies.size();
        int m = 0;

        for (int i = 0; i < n; i++)
        {
            m = max(m, candies[i]);
        }

        vector<bool> ans(n, true);

        for (int i = 0; i < n; i++)
        {
            if (candies[i] + extraCandies < m)
            {
                ans[i] = false;
            }

        }

        return ans;
    }
};
