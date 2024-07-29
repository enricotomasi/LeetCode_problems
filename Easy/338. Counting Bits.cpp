class Solution
{
public:
    int co(int n)
    {
        int ans = 0;

        while (n)
        {
            if (n % 2 == 1)
            {
                ans++;
            }

            n /= 2;
        }

        return ans;
    }
    
    vector<int> countBits(int n)
    {
        vector<int> ans(n + 1, 0);

        for (int i = 0; i <= n; i++)
        {
            ans[i] = co(i);
        }

        return ans;
    }
};