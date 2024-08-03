class Solution
{
public:
    int arrangeCoins(int n)
    {
        int ans = 0;

        int i = 1;
        while (n >= i)
        {
            // cout << endl;
            // cout << "n: " << n << endl;
            // cout << "i: " << i << endl;
            
            n -= i;
            ans++;

            i++;
        }

        return ans;
    }
};