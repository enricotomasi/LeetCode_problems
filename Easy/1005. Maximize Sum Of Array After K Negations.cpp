class Solution
{
public:
    int largestSumAfterKNegations(vector<int> &nums, int k)
    {
        vector<int> pos;
        vector<int> neg;

        for (auto it : nums)
        {
            if (it < 0)
            {
                neg.push_back(it);
            }
            else
            {
                pos.push_back(it);
            }
        }

        sort(neg.begin(), neg.end());
        sort(pos.begin(), pos.end());

        int np = pos.size();
        int nn = neg.size();

        int n = 0;

        while (k && n < nn)
        {
            neg[n] *= -1;
            k--;
            n++;
        }

        if (k > 0 && k % 2 != 0)
        {
            if (nn == 0)
            {
                pos[0] *= -1;
            }
            else if (np == 0)
            {
                neg[nn - 1] *= -1;
            }
            else if (neg[nn - 1] < pos[0])
            {
                neg[nn - 1] *= -1;
            }
            else
            {
                pos[0] *= -1;
            }
        }
        
        int ans = 0;

        for (auto it : pos) ans += it;
        for (auto it : neg) ans += it;

        return ans;
    }
};