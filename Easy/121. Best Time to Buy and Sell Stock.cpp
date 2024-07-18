class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int n = prices.size();
        int ans = 0;

        vector<int> m(n, 0);

        int temp = INT_MIN;

        for (int i = n - 1; i >= 0; i--)
        {
            temp = max(temp, prices[i]);
            m[i] = temp;
        }
        
        // for (auto it : m) cout << it << " ";
        // cout << endl;

        for (int i = 0; i < n; i++)
        {
            ans = max(ans, m[i] - prices[i]);
        }

        return ans;
    }
};