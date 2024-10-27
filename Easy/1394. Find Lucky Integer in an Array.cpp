class Solution
{
public:
    int findLucky(vector<int> &arr)
    {
        unordered_map<int, int> m;

        for (auto it : arr)
        {
            m[it]++;
        }

        int ans = -1;

        for (auto it : arr)
        {
            if (it == m[it])
            {
                ans = max(ans, it);
            }
        }

        return ans;
    }
};