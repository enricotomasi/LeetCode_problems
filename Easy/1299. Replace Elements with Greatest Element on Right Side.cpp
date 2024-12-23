class Solution
{
public:
    vector<int> replaceElements(vector<int> &arr)
    {
        int n = arr.size();

        vector<int> ans(n, 0);
        int m = -1;

        for (int i = n - 1; i >= 0; i--)
        {
            ans[i] = m;
            m = max(m, arr[i]);
        }

        return ans;
    }
};
