class Solution
{
public:
    int findLHS(vector<int> &nums)
    {
        unordered_map<int, int> m;

        for (auto it : nums)
        {
            m[it]++;
        }

        int ans = 0;

        for (auto it : m)
        {
            if (m.find(it.first + 1) != m.end())
            {
                int temp = m[it.first] + m[it.first + 1];
                ans = max(ans, temp);
            }
        }

        return ans;

    }
};